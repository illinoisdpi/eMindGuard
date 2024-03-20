<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = strip_tags(trim($_POST["name"]));
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = trim($_POST["message"]);

    // Specify the admin email where the message will be sent
    $admin_email = "skosar2@uic.edu";
    // Specify the email subject
    $subject = "New Contact Form Submission from $name";
    // Create the email headers
    $headers = "From: $name <$email>";

    // Build the email content
    $email_content = "Name: $name\n";
    $email_content .= "Email: $email\n\n";
    $email_content .= "Message:\n$message\n";

    // Send the email to admin
    mail($admin_email, $subject, $email_content, $headers);

    // Redirect to a thank-you page or back to the form page with a success message
    header("Location: thank-you.html");
} else {
    // Not a POST request, redirect to the form or home page
    header("Location: contact.html");
}

exit;
?>

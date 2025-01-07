document.getElementById("predict-button").addEventListener("click", () => {
    const getInputValue = (id) => {
        const value = document.getElementById(id).value.trim();
        // Convert to a float to ensure compatibility with backend processing
        return parseFloat(value) || 0; // Default to 0 if input is invalid
    };

    const formData = {
        socioEconomic: getInputValue("socioEconomic"),
        household: getInputValue("household"),
        behavioral: getInputValue("behavioral"),
        chronic: getInputValue("chronic"),
        wellBeing: getInputValue("wellBeing"),
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.score !== undefined) {
            document.getElementById("result").innerText = `Predicted Mental Health Score: ${data.score.toFixed(2)}`;
        } else {
            document.getElementById("result").innerText = "Error in prediction. Please try again.";
        }
    })
    .catch((error) => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "An error occurred while processing your request.";
    });
});
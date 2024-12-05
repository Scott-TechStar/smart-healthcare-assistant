async function getPrediction(event) {
    event.preventDefault();
    
    // Get form data
    const inputData = {
        age: parseInt(document.getElementById("age").value),
        weight: parseFloat(document.getElementById("weight").value),
        height: parseFloat(document.getElementById("height").value),
        fever: document.getElementById("fever").value === "yes" ? 1 : 0,
        cough: document.getElementById("cough").value === "yes" ? 1 : 0,
        headache: document.getElementById("headache").value === "yes" ? 1 : 0,
        chest_pain: document.getElementById("chest_pain").value === "yes" ? 1 : 0,
    };

    // Show loading spinner
    document.getElementById("loading-spinner").style.display = "flex";

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(inputData),
        });

        const result = await response.json();

        // Hide loading spinner
        document.getElementById("loading-spinner").style.display = "none";

        if (response.ok) {
            document.getElementById("prediction-output").textContent = `Prediction: ${result.prediction}`;
        } else {
            document.getElementById("prediction-output").textContent = `Error: ${result.error}`;
        }
    } catch (error) {
        document.getElementById("loading-spinner").style.display = "none";
        document.getElementById("prediction-output").textContent = `Error: Something went wrong. Please try again.`;
    }
}

document.getElementById("health-form").addEventListener("submit", getPrediction);

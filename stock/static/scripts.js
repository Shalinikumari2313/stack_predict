// static/script.js
document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const date = document.getElementById('date').value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ date: date })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        const resultDiv = document.getElementById('prediction-result');
        resultDiv.textContent = `Predicted Close Price: $${data.prediction.toFixed(2)}`;
    })
    .catch(error => console.error('Error:', error));
});

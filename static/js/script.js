document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const resultsDiv = document.getElementById('results');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(form);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultsDiv.innerHTML = `<p class="text-danger">Error: ${data.error}</p>`;
            } else {
                resultsDiv.innerHTML = `
                    <h2 class="text-success">Analysis Completed</h2>
                    <h3>Summary</h3>
                    <p>${data.summary}</p>
                    <h3>Document Type</h3>
                    <p>${data.document_type}</p>
                    <p>Results have been stored in a CSV file. You can download it from the link below:</p>
                    <a href="${data.csv_path}" class="btn btn-primary" download>Download Results</a>
                `;
            }
        })
        .catch(error => {
            resultsDiv.innerHTML = `<p class="text-danger">Error: ${error.message}</p>`;
        });
    });
});

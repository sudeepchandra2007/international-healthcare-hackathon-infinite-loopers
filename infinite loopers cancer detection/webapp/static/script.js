document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("file-input");
    const fileLabel = document.getElementById("file-label");
    const fileNameDisplay = document.getElementById("file-name");
    const submitBtn = document.getElementById("submit-btn");
    const imagePreview = document.getElementById("image-preview");
    const dropArea = document.getElementById("drop-area");
    const pastResultsBody = document.getElementById("past-results-body");

    let pastAnalyses = [];

    function handleFile(file) {
        if (!file) return;
        submitBtn.disabled = false;

        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            imagePreview.style.display = "block";
        };
        reader.readAsDataURL(file);

        fileNameDisplay.textContent = file.name;
        fileLabel.textContent = "Change Image";
    }

    fileInput.addEventListener("change", () => {
        handleFile(fileInput.files[0]);
    });

    dropArea.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropArea.classList.add("dragover");
    });

    dropArea.addEventListener("dragleave", () => {
        dropArea.classList.remove("dragover");
    });

    dropArea.addEventListener("drop", (e) => {
        e.preventDefault();
        dropArea.classList.remove("dragover");

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            handleFile(files[0]);
        }
    });

    submitBtn.addEventListener("click", async () => {
        const file = fileInput.files[0];
        if (!file) return;

        submitBtn.textContent = "Analyzing...";
        submitBtn.disabled = true;

        const formData = new FormData();
        formData.append("file", file);

        try {
            let response = await fetch("/analyze", {
                method: "POST",
                body: formData
            });

            let result = await response.json();

            document.getElementById("findings").textContent = result.findings;
            document.getElementById("concerns").textContent = result.concerns;
            document.getElementById("probability").textContent = result.probability;
            document.getElementById("cancer-type").textContent = result.cancer_type;

            let timestamp = new Date().toLocaleString();
            pastAnalyses.push({
                timestamp: timestamp,
                findings: result.findings,
                concerns: result.concerns,
                probability: result.probability,
                cancer_type: result.cancer_type
            });

            updatePastResultsTable();

        } catch (error) {
            console.error("Error:", error);
        } finally {
            submitBtn.textContent = "Analyze";
            submitBtn.disabled = false;
        }
    });

    function updatePastResultsTable() {
        pastResultsBody.innerHTML = "";
        pastAnalyses.forEach((entry) => {
            let row = document.createElement("tr");
            row.innerHTML = `
                <td>${entry.timestamp}</td>
                <td>${entry.findings}</td>
                <td>${entry.concerns}</td>
                <td>${entry.probability}</td>
                <td>${entry.cancer_type}</td>
            `;
            pastResultsBody.appendChild(row);
        });
    }
});

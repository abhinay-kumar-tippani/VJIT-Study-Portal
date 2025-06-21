const pdfList = document.getElementById("pdfList");

async function getData() {
    try {
        const response = await fetch("bee_pdf.json");
        const data = await response.json();

        data.forEach(pdf => {
            const li = document.createElement("li");
        li.innerHTML = `
        <span>${pdf.name}</span>
        <div class="btn-group">
        <a class="btn view-btn" href="${pdf.file}" target="_blank">View</a>
        <a class="btn download-btn" href="${pdf.file}" download>Download</a>
        </div>
        `
        pdfList.appendChild(li);
        });

    } catch (error) {
        pdfList.innerHTML = "<li>error in loading pdf's</li>"
    }
}

getData();
const pdfList = document.getElementById("pdfList");

fetch("pdfs.json")
  .then(response => response.json())
  .then(data => {
    data.forEach(pdf => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span>${pdf.name}</span>
        <div class="btn-group">
          <a class="btn view-btn" href="${pdf.file}" target="_blank">View</a>
          <a class="btn download-btn" href="${pdf.file}" download>Download</a>
        </div>
      `;
      pdfList.appendChild(li);
    });
  })
  .catch(error => {
    console.error("Error loading PDFs:", error);
    pdfList.innerHTML = "<li>Failed to load PDFs</li>";
  });

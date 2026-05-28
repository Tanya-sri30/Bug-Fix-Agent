async function analyzeCode() {

    const code = document.getElementById("codeInput").value;
     const language = document.getElementById("language").value;

    const resultBox = document.getElementById("result");

    resultBox.innerHTML = `
    <div class="spinner"></div>
    <p>Analyzing Code...</p>
`;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
      

body: JSON.stringify({
    code: code,
    language: language
})
    });

    const data = await response.json();

    resultBox.innerText = data.response;
}
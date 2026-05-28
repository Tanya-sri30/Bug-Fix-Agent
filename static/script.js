async function analyzeCode() {

    const code = document.getElementById("codeInput").value;

    const resultBox = document.getElementById("result");

    resultBox.innerText = "Analyzing...";

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code
        })
    });

    const data = await response.json();

    resultBox.innerText = data.response;
}
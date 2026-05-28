from flask import Flask, render_template, request, jsonify
from services.gemini_service import analyze_bug

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    code = data.get("code")

    result = analyze_bug(code)

    return jsonify({
        "response": result
    })


if __name__ == "__main__":
    app.run(debug=True)
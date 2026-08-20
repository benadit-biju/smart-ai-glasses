from flask import Flask, request, jsonify

app = Flask(__name__)

def ai_response(text: str) -> str:
    """
    Replace this demo function with your preferred AI model/API.

    Possible integrations:
    - Gemini API
    - OpenAI API
    - Local LLM
    - Speech-to-text + LLM pipeline
    """
    text = text.strip()

    if not text:
        return "I did not receive a request."

    return f"Demo AI response: received '{text[:60]}'"

@app.post("/ask")
def ask():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    return jsonify({"response": ai_response(text)})

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "smart-ai-glasses"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

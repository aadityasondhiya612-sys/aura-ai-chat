from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Gemini API key (Render se aayega)
API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    data = {
        "contents": [{
            "parts": [{"text": user_msg}]
        }]
    }

    response = requests.post(url, json=data)
    result = response.json()

    try:
        reply = result['candidates'][0]['content']['parts'][0]['text']
    except:
        reply = "⚠️ Error aa gaya, phir try karo"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

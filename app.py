from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json['message']
    reply = "Tumne likha: " + user_msg
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()

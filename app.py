from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from nova_core import ask_nova

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")  # Load the HTML UI from templates folder

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()

    print("➡️ User said:", user_input)

    if not user_input:
        return jsonify({"response": "Please enter a valid message."})

    reply = ask_nova(user_input)
    print("🧠 Nova-X replied:", reply)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)

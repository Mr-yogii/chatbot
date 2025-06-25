from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from time import time

app = Flask(__name__)

genai.configure(api_key="AIzaSyA55SoWZ5IcBNqbJrbUHbVLOKrzHERzesg") 
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

active_chats = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start_chat", methods=["POST"])
def start_chat():
    session_id = str(int(time() * 1000))
    active_chats[session_id] = model.start_chat()
    return jsonify({"session_id": session_id})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    user_input = data.get("input", "")
    session_id = data.get("session_id", "")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    if session_id not in active_chats:
        return jsonify({"error": "Invalid session"}), 400
    
    try:
        response = active_chats[session_id].send_message(user_input)
        return jsonify({
            "response": response.text,
            "session_id": session_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

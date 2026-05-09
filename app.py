import os
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/")
def index():
    return send_from_directory(Path.cwd(), "index.html")

@app.route("/api/command", methods=["POST"])
def command():
    payload = request.get_json(silent=True) or {}
    command_text = payload.get("command", "").strip()

    if not command_text:
        return jsonify(response="Please send a command."), 400

    # Replace this placeholder logic with your own AI or command-handling code.
    response_text = (
        "Hello! I received your command. Replace this handler with real logic."
        if command_text.lower() == "hello"
        else f"Received command: {command_text}."
    )

    return jsonify(response=response_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

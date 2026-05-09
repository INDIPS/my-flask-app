import os
import subprocess
import json

import pyttsx3

try:
    import psutil  # type: ignore
except ImportError:
    psutil = None  # type: ignore

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder=".", static_url_path="")

# File upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mp3', 'doc', 'docx', 'xls', 'xlsx', 'zip', 'csv', 'json'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Initialize TTS engine
try:
    engine = pyttsx3.init()
    # Select a more natural voice if available (e.g., Microsoft Zira)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "zira" in voice.name.lower() or "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 175) # 175-200 range sounds more human than 150
except Exception as e:
    print(f"TTS initialization failed: {e}")
    engine = None

# Online AI configuration (Set these in your environment variables)
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-4')
OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE', 'https://api.openai.com/v1')
OPENAI_SYSTEM_PROMPT = os.environ.get(
    'OPENAI_SYSTEM_PROMPT',
    'You are JARVIS, an intelligent assistant. Answer clearly, concisely, and respectfully.'
)

LOCAL_ACTIONS = {
    'open chrome': lambda: subprocess.Popen('start chrome', shell=True),
    'open notepad': lambda: subprocess.Popen('notepad'),
}

def speak(text):
    """Text-to-speech function"""
    print(f"JARVIS: {text}")
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass

def query_ai_server(prompt):
    """Send the user prompt to the online AI server using OpenAI Python SDK with fallback models."""
    if not OPENAI_API_KEY:
        return 'Online AI server is not configured. Please set the OPENAI_API_KEY environment variable.'

    if OpenAI is None:
        return 'OpenAI Python SDK is not installed. Please install it with pip install openai.'

    # Model fallback order: preferred model, then gpt-5.5, then gpt-3.5-turbo
    models_to_try = [OPENAI_MODEL, 'gpt-5.5', 'gpt-3.5-turbo']
    # Remove duplicates in case OPENAI_MODEL is already one of the fallbacks
    models_to_try = list(dict.fromkeys(models_to_try))

    for model in models_to_try:
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.responses.create(
                model=model,
                input=[
                    {
                        'role': 'system',
                        'content': OPENAI_SYSTEM_PROMPT,
                    },
                    {
                        'role': 'user',
                        'content': prompt,
                    },
                ],
                temperature=0.6,
                max_output_tokens=500,
            )

            # The outputs can be combined text or structured objects.
            if hasattr(response, 'output_text') and response.output_text:
                return response.output_text.strip()

            # Fallback for structured output
            if getattr(response, 'output', None):
                chunks = []
                for item in response.output:
                    if getattr(item, 'content', None):
                        for content_item in item.content:
                            if getattr(content_item, 'text', None):
                                chunks.append(content_item.text)
                if chunks:
                    return ' '.join(chunks).strip()

            return 'No valid response received from the AI server.'
        except Exception as e:
            error_msg = str(e).lower()
            # If it's a model not found error, try the next model
            if 'model' in error_msg and ('not found' in error_msg or 'does not exist' in error_msg):
                continue
            # For other errors (like quota, auth), don't retry
            return f"AI request failed: {str(e)}"

    # If all models failed
    return 'All AI models are currently unavailable. Please try again later.'

def process_command(command):
    """Determine if command is local, system-related, or needs AI."""
    normalized = command.lower().strip()

    # Local Actions
    for trigger, action in LOCAL_ACTIONS.items():
        if trigger in normalized:
            try:
                action()
                return f'Executed local action: {trigger}.'
            except Exception:
                return f'Unable to execute local action: {trigger}.'

    # System Status
    if any(key in normalized for key in ['cpu', 'memory', 'disk', 'system']):
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return f'System status: CPU {cpu}%, memory {memory.percent}%, disk {disk.percent}%.'

    # Default to AI Assistant
    return query_ai_server(command)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return send_from_directory(Path.cwd(), "index.html")

@app.route("/uploads/<filename>")
def serve_upload(filename):
    return send_from_directory(UPLOAD_FOLDER, secure_filename(filename))

@app.route("/api/upload", methods=["POST"])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify(error="No file provided"), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify(error="No file selected"), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            return jsonify(
                success=True,
                filename=filename,
                url=f"/uploads/{filename}"
            ), 200
        else:
            return jsonify(error="File type not allowed"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route("/api/command", methods=["POST"])
def command():
    payload = request.get_json(silent=True) or {}
    command_text = payload.get("command", "").strip()

    if not command_text:
        return jsonify(response="Please send a command."), 400

    print(f"User: {command_text}")
    response_text = process_command(command_text)
    
    # Attempt to speak the response
    speak(response_text)

    return jsonify(response=response_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

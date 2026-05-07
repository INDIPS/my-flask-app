import os
import subprocess
import datetime
import psutil
import pyttsx3
import json
import urllib.request
import urllib.error
from flask import Flask, request, jsonify
from pathlib import Path

# Initialize Flask
app = Flask(__name__)

# Load TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Online AI configuration
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-3.5-turbo')
OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE', 'https://api.openai.com/v1')
OPENAI_SYSTEM_PROMPT = os.environ.get(
    'OPENAI_SYSTEM_PROMPT',
    'You are JARVIS, an intelligent assistant. Answer clearly, concisely, and respectfully. Use the online AI server to answer questions and do not fabricate API keys or unsupported actions.'
)

LOCAL_ACTIONS = {
    'open chrome': lambda: subprocess.Popen('start chrome', shell=True),
    'open notepad': lambda: subprocess.Popen('notepad'),
}

def speak(text):
    """Text-to-speech function"""
    print(f"JARVIS: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass


def query_ai_server(prompt):
    """Send the user prompt to the online AI server and return the response."""
    if not OPENAI_API_KEY:
        return (
            'Online AI server is not configured. Set OPENAI_API_KEY in your environment and restart the app.'
        )

    payload = {
        'model': OPENAI_MODEL,
        'messages': [
            {'role': 'system', 'content': OPENAI_SYSTEM_PROMPT},
            {'role': 'user', 'content': prompt},
        ],
        'temperature': 0.6,
        'max_tokens': 500,
    }
    data = json.dumps(payload).encode('utf-8')
    url = f"{OPENAI_API_BASE}/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}',
    }

    try:
        request_obj = urllib.request.Request(url, data=data, headers=headers, method='POST')
        with urllib.request.urlopen(request_obj, timeout=30) as response:
            response_text = response.read().decode('utf-8')
            result = json.loads(response_text)
            return result['choices'][0]['message']['content'].strip()

    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        print(f'AI request failed: {e.code} {e.reason} {error_body}')
        return 'The online AI server returned an error. Check your API key and configuration.'
    except urllib.error.URLError as e:
        print(f'AI request failed: {e}')
        return 'Unable to reach the online AI server. Check your internet connection.'
    except Exception as e:
        print(f'AI request failed: {e}')
        return 'An unexpected error occurred while contacting the AI server.'


def process_command(command):
    """Process the user command, perform local actions when needed, otherwise query the AI server."""
    normalized = command.lower().strip()

    for trigger, action in LOCAL_ACTIONS.items():
        if trigger in normalized:
            try:
                action()
                return f'Executed local action: {trigger}.'
            except Exception:
                return f'Unable to execute local action: {trigger}.'

    if 'cpu' in normalized or 'memory' in normalized or 'disk' in normalized or 'system' in normalized:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return f'System status: CPU {cpu}%, memory {memory.percent}%, disk {disk.percent}%.'

    if 'shutdown' in normalized or 'exit' in normalized or 'stop' in normalized:
        return 'This command is blocked for safety in the web interface.'

    return query_ai_server(command)

# WEB ROUTES
@app.route('/')
def index():
    """Serve the HTML interface"""
    html_path = Path(__file__).parent / 'index.html'
    if html_path.exists():
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "HTML file not found"

@app.route('/api/command', methods=['POST'])
def handle_command():
    """Handle commands from web interface"""
    try:
        data = request.get_json()
        command = data.get('command', '')
        
        print(f"User: {command}")
        response = process_command(command)
        
        # Try text-to-speech
        try:
            speak(response)
        except:
            pass
        
        return jsonify({'response': response, 'status': 'success'})
    
    except Exception as e:
        error_msg = f"Error processing command: {str(e)}"
        print(error_msg)
        return jsonify({'response': 'Sorry, something went wrong.', 'status': 'error', 'error': error_msg}), 500

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🤖 JARVIS AI ASSISTANT")
    print("="*50)
    print("Starting web server...")
    print("Open your browser and go to: http://localhost:5000")
    print("="*50 + "\n")
    
    try:
        app.run(debug=True, port=5000, use_reloader=False)
    except KeyboardInterrupt:
        print("\nShutting down JARVIS...")
        exit()
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
print("[OK] .env loaded")

from routes.chat_routes import chat_bp
from config.gemini import ai_service

# Serve static files from the frontend directory
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# API Routes
app.register_blueprint(chat_bp, url_prefix='/api/chat')

# Health Check Route
@app.route('/health', methods=['GET'])
def health():
    if getattr(ai_service, 'mock_mode', False):
        return jsonify({
            "backend": "running",
            "ai": "mocked"
        }), 200
        
    if ai_service.error_reason:
        return jsonify({
            "backend": "running",
            "ai": "failed",
            "reason": ai_service.error_reason
        }), 500
    return jsonify({
        "backend": "running",
        "ai": "connected"
    }), 200

# Compliance Check-in Route
@app.route('/checkin', methods=['POST'])
def checkin():
    return jsonify({"success": True, "message": "Check-in received"}), 200

# Root route
@app.route('/')
def index():
    return app.send_static_file('chat.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print("[OK] Server started")
    print(f"Health Assistant Chatbot server running on http://localhost:{port}")
    print(f"API endpoint: http://localhost:{port}/api/chat")
    
    # Start the server
    app.run(host='0.0.0.0', port=port, debug=True)

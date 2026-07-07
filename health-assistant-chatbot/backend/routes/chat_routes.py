from flask import Blueprint
from controllers.chat_controller import handle_chat

chat_bp = Blueprint('chat', __name__)

# POST /api/chat - Send message and get response
@chat_bp.route('/', methods=['POST'], strict_slashes=False)
def chat():
    return handle_chat()

"""A Chatbot instance"""
# pylint: disable-next=missing-module-docstring
from flask import jsonify, request, Blueprint
from ai_application.chat import chat

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.get('/')
def chatbot_index():
    """Returns the initial chatbot resonse"""
    return jsonify({
        "status": 200,
        "message": "Welcome to the AI-Flask Chatbot!"
    })

@chatbot_bp.post('/predict')
def predict():
    """After JSON \"message\" is sent, returns the chatbot response."""
    text = request.get_json().get("message") # error check text is valid
    response = chat.get_response(text)
    return jsonify({
        "status": 200,
        "answer": response
    }), 200

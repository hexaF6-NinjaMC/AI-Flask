"""A Chatbot instance"""
# pylint: disable-next=missing-module-docstring
from flask import jsonify, request, Blueprint
from ai_application.chat import chat

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.get('/')
def chatbot_index():
    """Returns the initial chatbot response"""
    return jsonify({
        "status": 200,
        "answer": "Welcome to the AI-Flask Chatbot!"
    })

@chatbot_bp.post('/predict')
def predict():
    """After JSON \"message\" is sent, returns the chatbot response."""
    text = request.get_json()
    if not text.get("message"):
        return jsonify({
            "status": 422,
            # pylint: disable-next=line-too-long
            "answer": "The request object does not follow the expected format.\nJSON data must have \"message\" as key."
        }), 422
    text = text.get("message")
    response = chat.get_response(text)
    return jsonify({
        "status": 200,
        "answer": response
    }), 200

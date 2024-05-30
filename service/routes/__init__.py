"""Register all route Blueprints in this catch-all Blueprint for the whole application."""
from flask import Blueprint, abort, jsonify
from service.chatbot import chatbot_bp
from service.auth import auth_bp
from service.upload_training_data import upload_bp

# Flask Blueprint
app_bp = Blueprint("app_bp", __name__, root_path="/")
app_bp.register_blueprint(chatbot_bp, url_prefix="/chatbot")
app_bp.register_blueprint(auth_bp)
app_bp.register_blueprint(upload_bp)

# ==============---------------RESPONSES---------------==============

# =================================================================
# For Error testing:
@app_bp.get('/error/<int:err_no>')
def show_error(err_no):
    """
    Used to test error handling
    """
    abort(err_no)
# =================================================================

# Home page
@app_bp.get("/")
def index():
    """
    Home page
    """
    return jsonify({
        "status": 200,
        "message": "Welcome to the AI-Flask App!"
    }), 200

# GET AI response:
@app_bp.get("/response")
def get_ai_response():
    """
    GET AI response
    """
    return jsonify({
        "status": 200,
        "message": "Here is your information about the AI-Flask App response."
    }), 200

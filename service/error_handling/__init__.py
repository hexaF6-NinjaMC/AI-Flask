"""Contains all error handling responses"""
from flask import Blueprint, jsonify

error_bp = Blueprint('error_bp', __name__, root_path='/')

# ==============---------------ERROR HANDLERS---------------==============

# =================================================================
# 500-LEVEL ERROR HANDLERS

# 500 - Internal Server Error
@error_bp.app_errorhandler(500)
# pylint: disable-next=unused-argument
def server_error(e):
    """
    Used when a server error occurs during execution
    """
    return jsonify({
        "status": 500,
        "message": "Internal error: the server was unable to complete your request."
    }), 500

# =================================================================
# 400-LEVEL ERROR HANDLERS

# 405 - Permission Request Denied
@error_bp.app_errorhandler(405)
# pylint: disable-next=unused-argument
def method_not_allowed(e):
    """
    Used when denied access: lacks permissions
    """
    return jsonify({
        "status": 405,
        "message": "This method is not applicable to the functionality of the application."
    }), 405

# 404 - Invalid URL
@error_bp.app_errorhandler(404)
# pylint: disable-next=unused-argument
def page_not_found(e):
    """
    Used when the requested URL and/or content was not found on the server
    """
    return jsonify({
        "status": 404,
        "message": "The requested URL/content was not found on the server."
    }), 404

# 422 - Unprocessable Entity
@error_bp.app_errorhandler(422)
# pylint: disable-next=unused-argument
def unprocessable_entity(e):
    """
    Used when request object doesn't follow the expected format
    """
    return jsonify({
        "status": 422,
        "message": "The request object does not follow the expected format."
    }), 422

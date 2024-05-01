"""Contains all error handling responses"""
from flask import Blueprint, jsonify

error_bp = Blueprint('error_bp', __name__, root_path='/')

# ==============---------------ERROR HANDLERS---------------==============

# =================================================================
# 500-LEVEL ERROR HANDLERS

# 500 - Internal Server Error
@error_bp.app_errorhandler(500)
def server_error():
    """
    Used when a server error occurs during execution
    """
    return jsonify({
        "status": 500,
        "message": "Internal error: the server was unable to complete your request."
    }), 500

# =================================================================
# 400-LEVEL ERROR HANDLERS

# 401 - Unauthenticated Access
@error_bp.app_errorhandler(401)
def unauthenticated_access():
    """
    Used when denied access: lacks credentials
    """
    return jsonify({
        "status": 401,
        "message": "You are not authorized to perform this action."
    }), 401

# 403 - Permission Request Denied
@error_bp.app_errorhandler(403)
def access_denied():
    """
    Used when denied access: lacks permissions
    """
    return jsonify({
        "status": 403,
        "message": "You are not authorized to perform this action."
    }), 403

# 404 - Invalid URL
@error_bp.app_errorhandler(404)
def page_not_found():
    """
    Used when the requested URL and/or content was not found on the server
    """
    return jsonify({
        "status": 404,
        "message": "The requested URL/content was not found on the server."
    }), 404

# 422 - Unprocessable Entity
@error_bp.app_errorhandler(422)
def unprocessable_entity():
    """
    Used when request object doesn't follow the expected format
    """
    return jsonify({
        "status": 422,
        "message": "The request object does not follow the expected format."
    }), 422

from flask import Blueprint, abort, jsonify

# Flask Blueprint
app_bp = Blueprint('app_bp', __name__, root_path='/')

# ==============---------------PAGE RENDERS---------------==============
# For Error testing:
@app_bp.route('/error/<int:err_no>')
def show_error_page(err_no):
    """
    Used to test error handling
    """
    abort(err_no)

# Home page
@app_bp.route("/")
def index():
    """
    Home page
    """
    return jsonify({
        "status": 200,
        "message": "Welcome to the AI-Flask App!"
    })

# ==============---------------PAGE ERROR HANDLERS---------------==============
# Invalid URL
@app_bp.app_errorhandler(404)
def page_not_found(e):
    """
    Used when the requested URL and/or content was not found on the server
    """
    return jsonify({
        "status": 404,
        "message": "The requested URL/content was not found on the server. If you entered the URL manually please check your spelling and try again."
    })

# Internal Server Error
@app_bp.app_errorhandler(500)
def server_error(e):
    """
    Used when a server error occurs during execution
    """
    return jsonify({
        "status": 500,
        "message": "The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application."
    })

# Permission Request Denied
@app_bp.app_errorhandler(403)
def access_denied(e):
    """
    Used when denied access: lacks permissions
    """
    return jsonify({
        "status": 403,
        "message": "You are not authorized to perform this action."
    })

# Unauthenticated Access
@app_bp.app_errorhandler(401)
def unauthenticated_access(e):
    """
    Used when denied access: lacks credentials
    """
    return jsonify({
        "status": 401,
        "message": "You are not authorized to perform this action."
    })
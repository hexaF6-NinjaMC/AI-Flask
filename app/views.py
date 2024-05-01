from flask import Blueprint, abort, render_template, flash

# Flask Blueprint
app_bp = Blueprint('app_bp', __name__, template_folder='/templates', root_path='/')

# ==============---------------PAGE RENDERS---------------==============
# For Error page views testing:
@app_bp.route('/error/<int:err_no>')
def show_error_page(err_no):
    abort(err_no)

# Home page
@app_bp.route("/")
def main():
    return render_template('index.html'), 200

# ==============---------------PAGE ERROR HANDLERS---------------==============
# Invalid URL
@app_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app_bp.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Permission Request Denied
@app_bp.app_errorhandler(403)
def access_denied(e):
    flash("You are not authorized to perform this action.", category="error")
    return render_template('403.html'), 403
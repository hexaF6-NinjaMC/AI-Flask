"""Add File Upload routes"""
#pylint: disable=line-too-long
import os
from flask import Blueprint, current_app, flash, make_response, redirect, render_template, request
from flask_login import login_required
from werkzeug.utils import secure_filename
from service.forms import FileUploadForm
from ai_application.train.train import train_chatbot

upload_bp = Blueprint('upload_bp', __name__)

@upload_bp.get('/upload')
@login_required
def upload_file():
    """Returns the initial file upload response"""
    form = FileUploadForm()
    response = make_response(render_template('upload.html', form=form))
    return response

@upload_bp.post('/upload')
@login_required
def upload_file_post():
    """Attempts to upload the file and train the model on save"""
    print("Upload file attempt")
    form = FileUploadForm()
    if form.validate_on_submit():
        file = request.files['file']
        if file.filename == '':
            flash('No selected file.')
            return redirect("/upload")
        secure_file = secure_filename(file.filename)
        print(f"Uploading file...\n    > {os.path.join(current_app.config['UPLOAD_FOLDER'], secure_file)}")
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_file))
        print(f"Saved file:\n    > {os.path.join(current_app.config['UPLOAD_FOLDER'], secure_file)}")
        flash('File successfully uploaded.')
        train_chatbot()
    return redirect("/upload")

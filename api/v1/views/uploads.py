#!/usr/bin/python3
"""Holds all RESTAPI for uploads"""
import os
from models import storage
from models.logo import Logo
from models.video import Video
from models.video import Video
from api.v1.views import app_views
from flask import Flask, abort, jsonify, make_response, request, flash, current_app, send_from_directory
from werkzeug.utils import secure_filename
from uuid import uuid4
from api.v1.app import app



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowd_file(filename):
    """Checks the file is in the list of allowd files"""
    return '.' in filename and \
                       filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app_views.route('/uploadlogo', methods=['POST'], strict_slashes=False)
def upload_logo():
    """uploads logo"""
    if 'UPLOAD_FOLDER' not in current_app.config:
        print("missing folder")
        abort(500, description="UPLOAD_FOLDER is not configured")
    if request.method == "POST":
        # check if post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            abort(400, description="Missing file")
        file = request.files['file']
        #if an empty file was submitted
        if file.filename == '':
            print("Empty file")
            flash("No selected file")
            abort(400, description="No file provided")
        if 'business_id' not in request.form:
            abort(400, description="Missing business_id")
        business_id = request.form.get("business_id")
        if file and allowd_file(file.filename):
            filename = secure_filename(file.filename)
            unique_file = f"{str(uuid4())}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_file))
            instance = Logo(url=unique_file)
            instance.business_id = business_id
            instance.save()
            return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('uploads/<filename>', methods=['GET'], strict_slashes=False)
def uploaded_file(filename):
    """Get uploads content from dir"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



EXTENSIONS_ALLOWED = {'mp4', 'webm', 'ogg'}

def allowd_format(filename):
    """Checks the file is in the list of allowd files"""
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in EXTENSIONS_ALLOWED



@app_views.route('/uploadvideo', methods=['POST'], strict_slashes=False)
def upload_video():
    """uploads a video to the upload_folder"""
    if request.method == "POST":
        #check if post reqest has the file part
        if 'file' not in request.files:
            flash('No file part')
            abort(400, description="Missing file")
        file = request.files['file']
        #if an empty file was submitted
        if file.filename == '':
            flash("No selected file")
            abort(400, description="No file provided")
        if 'business_id' not in request.form:
            abort(400, description="Missing bsiness_id")
        business_id = request.form.get("business_id")
        description = request.form.get("description")
        if file and allowd_format(file.filename):
            filename = secure_filename(file.filename)
            unique_file = f"{str(uuid4())}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_file))
            instance = Video(url=unique_file)
            instance.business_id = business_id
            instance.description = description
            instance.save()
            return make_response(jsonify(instance.to_dict()), 201)

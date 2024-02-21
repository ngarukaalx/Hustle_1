#!/usr/bin/python3
"""Flask Application"""

import os
from models import storage
from models.user import User
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '0712408072'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
app.debug = True

CORS(app, resources={r"/api/v1/*": {"origins": "*"}}, supports_credentials=True)
# Specify an absolute path for the upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.teardown_appcontext
def close_db(error):
    """Close Storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Error 404, when a resource is not found"""
    return make_response(jsonify({'Error': "Not found"}), 404)


@login_manager.user_loader
def load_user(user_id):
    """Get user object by id"""
    print("Am beibg called user_loader")
    return storage.get(User, user_id)


if __name__ == "__main__":
    """main fuction"""
    host = environ.get('HSTL_API_HOST')
    port = environ.get('HSTL_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

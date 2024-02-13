#!/usr/bin/python3
"""Flask Application"""

from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
login_manager = LoginManager(app)
app.debug = True
from flask_cors import CORS

CORS(app, resources={r"/api/v1/*": {"origins": "http://localhost:8080", "supports_credentials": True, "headers": "Content-Type"}})


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
    return storage.get(user_id)


if __name__ == "__main__":
    """main fuction"""
    host = environ.get('HSTL_API_HOST')
    port = environ.get('HSTL_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)

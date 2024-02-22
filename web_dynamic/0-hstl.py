#!/usr/bin/python3
"""Starts a flask web application"""
from os import environ
import uuid
from flask import Flask, render_template
app = Flask(__name__)
app.debug = True
cache_id = str(uuid.uuid4())

@app.route('/0-hstl/', strict_slashes=False)
def hstl():
    """rendiring live"""

    return render_template('home_hustle.html', cache_id=cache_id)

@app.route('/image', strict_slashes=False)
def images():
    """making image page live"""
    return render_template('images.html', cache_id=cache_id)


@app.route('/register', strict_slashes=False)
def register():
    """register page live"""
    return render_template('register.html', cache_id=cache_id)


@app.route('/register-biz', strict_slashes=False)
def biz():
    """register business live"""
    return render_template('register_biz.html', cache_id=cache_id)


@app.route('/user_page', strict_slashes=False)
def user():
    """User biz"""
    return render_template('user_page.html', cache_id=cache_id)


@app.route('/about', strict_slashes=False)
def about():
    """about live"""
    return render_template('about.html', cache_id=cache_id)


if __name__ == "__main__":
    """main fuction"""
    app.run(host='0.0.0.0', port=5000)

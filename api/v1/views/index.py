#!/usr/bin/python3
"""Status of application"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.county import County
from models.town import Town
from models.business import Business
from models.user import User
from models.video import Video
from models.image import Image
from models.category import Category


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Status of API"""
    return jsonify({"halihalisi": "mambo freshi"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def each_object():
    """retrieves the number of each objects by type"""
    classes = [County, Town, User, Business, Video, Image, Category]
    names = ["counties", "towns", "users", "businesses", "videos", "images", "categories"]

    all_objects = {}
    for i in range(len(classes)):
        all_objects[names[i]] = storage.count(classes[i])

    return jsonify(all_objects)

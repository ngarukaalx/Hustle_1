#!/usr/bin/python3
"""Holds all RESTAPI for category"""
from models import storage
from models.category import Category
from api.v1.views import app_views
from flask import abort, make_response, jsonify, request

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """Retrive all categoreies"""
    categories = storage.all(Category).values()
    list_category = []
    for category in categories:
        list_category.append(category.to_dict())
    return jsonify(list_category)


@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """Retrive a category"""
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    return jsonify(category.to_dict())


@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """Delete category"""
    category = storage.get(Category, category_id)
    if not category:
        abort(404)
    storage.delete(category)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def create_category():
    """creteas a category"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    instance = Category(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('categories/<category_id>', methods=['PUT'], strict_slashes=False)
def updates_category(category_id):
    """updates a category"""
    category = storage.get(Category, category_id)
    if not request.get_json():
        abort(400, description="Not a JSON")
    avoid = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(category, key, value)
    storage.save()
    return make_response(jsonify(category.to_dict()), 200)

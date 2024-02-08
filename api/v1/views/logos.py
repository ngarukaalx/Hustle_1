#!/usr/bin/python3
"""Holds all RESTAPI for logo"""
from models import storage
from models.logo import Logo
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/businesses/<business_id>/logo', methods=['POST'], strict_slashes=False)
def create_logo(business_id):
    """Creates a logo for a business"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'url' not in request.get_json():
        abort(400, description="Missing url")
    data = request.get_json()
    instance = Logo(**data)
    instance.business_id = business_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/logo/<logo_id>', methods=['DELETE'], strict_slashes=False)
def delete_logo(logo_id):
    """Deletes a logo"""
    logo = storage.get(Logo, logo_id)
    if not logo:
        abort(404)
    storage.delete(logo)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/logo/<logo_id>', methods=['PUT'], strict_slashes=False)
def updates_logo(logo_id):
    """Updates a logo"""
    logo = storage.get(Logo, logo_id)
    if not logo:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'url' not in request.get_json():
        abort(400, "Missing url")
    ignore = ['id', 'created_at', 'updated_at', 'business_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(logo, key, value)
    storage.save()
    return make_response(jsonify(logo.to_dict()), 201)

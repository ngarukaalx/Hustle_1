#!/usr/bin/python3
"""Handles all default RESTAPI for town"""

from models import storage
from models.town import Town
from models.county import County
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/counties/<county_id>/towns', methods=['GET'], strict_slashes=False)
def get_town(county_id):
    """Get all towns related to a specific county"""

    list_towns = []
    print("yes")
    county = storage.get(County, county_id)
    print("County:", county)
    if not county:
        return jsonify({"Error": "No town related to this county"}), 404
    for town in county.towns:
        list_towns.append(town.to_dict())

    return jsonify(list_towns)

@app_views.route('/towns/<town_id>', methods=['GET'], strict_slashes=False)
def retrive_city(town_id):
    """Retrives a town"""
    towns = storage.get(Town, town_id)
    if not towns:
        abort(404)
    return jsonify(towns.to_dict())


@app_views.route('/towns', methods=['GET'], strict_slashes=False)
def get_all_towns():
    """Get all towns"""
    all_towns = storage.all(Town).values()
    list_towns = []
    for town in all_towns:
        list_towns.append(town.to_dict())
    return jsonify(list_towns)


@app_views.route('/towns/<town_id>', methods=['DELETE'], strict_slashes=False)
def delete_town(town_id):
    """Delete a town"""
    town = storage.get(Town, town_id)
    if not town:
        abort(404)
    storage.delete(town)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/counties/<county_id>/towns', methods=['POST'], strict_slashes=False)
def create_town(county_id):
    """Create a town"""
    county = storage.get(County, county_id)
    if not county:
        abort(404)
    if not request.get_json():
        abort(404, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Town(**data)
    instance.county_id = county.id
    instance.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/towns/<town_id>', methods=['PUT'], strict_slashes=False)
def update_town(town_id):
    """Updates a town"""
    town = storage.get(Town, town_id)
    if not town:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")
    avoid = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(town, key, value)
    storage.save()
    return make_response(jsonify(town.to_dict()), 200)

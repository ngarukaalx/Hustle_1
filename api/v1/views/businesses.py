#!/usr/bin/python3
"""Holds all RESTAPI for business"""
from models import storage
from models.business import Business
from models.county import County
from models.user import User
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/business', methods=['GET'], strict_slashes=False)
def get_businesses():
    """Retrive all businesses"""
    list_business = [business.to_dict() for business in storage.all(Business).values()]
    return jsonify(list_business)

@app_views.route('/business/<user_id>', methods=['GET'], strict_slashes=False)
def get_business_forid(user_id):
    """Retrive business for a user"""
    all_business = [business.to_dict() for business in storage.all(Business).values() if business.user_id == user_id]
    if not all_business:
        return jsonify({"Error": "No business for this user"}), 404
    return jsonify(all_business)


@app_views.route('/businesses/<business_id>', methods=['GET'], strict_slashes=False)
def get_business(business_id):
    """Retrive a business by id"""
    business = storage.get(Business, business_id)
    if not business:
        abort(404)
    return jsonify(business.to_dict())


@app_views.route('/county/<county_id>/businesses', methods=['GET'], strict_slashes=False)
def get_busine_for_county(county_id):
    """Retrive a businesses that belongs to a county"""
    all_business = [business.to_dict() for business in storage.all(Business).values() if business.county_id == county_id]
    if not all_business:
        return jsonfy({"Error": "No business found for specified county"}), 404
    return jsonify(all_business)


@app_views.route('/town/<town_id>/businesses', methods=['GET'], strict_slashes=False)
def get_business_for_town(town_id):
    """Retrive businesses for a specific town"""
    all_business = [business.to_dict() for business in storage.all(Business).values() if business.town_id == town_id]
    if not all_business:
        return jsonify({"Error": "No business found for specified town"}), 404
    return jsonify(all_business)


@app_views.route('/businesses/<business_id>', methods=['DELETE'], strict_slashes=False)
def delete_business(business_id):
    """Deletes a business"""
    business = storage.get(Business, business_id)
    if not business:
        abort(404)
    storage.delete(business)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/county/<county_id>/town/<town_id>/user/<user_id>/businesses', methods=['POST'], strict_slashes=False)
def creates_busines1(county_id, town_id, user_id):
    """Creates a business with both county and business id"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    instance = Business(**data)
    instance.county_id = county_id
    instance.town_id = town_id
    instance.user_id = user_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/createbiz', methods=['POST'], strict_slashes=False)
def creates_busines2():
    """Creates a business with county_id and user_id"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    instance = Business(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/county/<county_id>/town/<town_id>/user/<user_id>/category/<category_id>/businesses', methods=['POST'], strict_slashes=False)
def create_business3(county_id, town_id, user_id, category_id):
    """Creates a user with county_id, town_id, user_id, and category_id"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Missing name")
    data = request.get_json()
    instance = Business(**data)
    instance.county_id = county_id
    instance.town_id = town_id
    instance.user_id = user_id
    instance.category_id = category_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/county/<county_id>/user/<user_id>/category/<category_id>businesses', methods=['POST'], strict_slashes=False)
def create_business4(county_id, user_id, category_id):
    """Creates a user with couty, user and category id"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'name' not in request.get_json():
        abort(400, description="Misssing name")
    data = request.get_json()
    instance = Business(**data)
    instance.county_id = county_id
    instance.user_id = user_id
    instance.category_id = category_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/businesses/<business_id>', methods=['PUT'], strict_slashes=False)
def updates_business(business_id):
    """updates a business"""
    business = storage.get(Business, business_id)
    if not request.get_json():
        abort(400, description="Not a JSON")
    avoid = ['id', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(business, key, value)
    storage.save()
    return make_response(jsonify(business.to_dict()), 200)

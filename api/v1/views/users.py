#!/usr/bin/pyhton3
"""Holds all RESTAPI for user"""
from models import storage
from models.user import User
from models.county import County
from models.town import Town
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flask_login import login_user, current_user, logout_user, login_required
from flask import session


@app_views.route('/logout', methods=['POST'], strict_slashes=False)
def logout():
    """logs out the current user"""
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200


@app_views.route('/user_id', methods=['POST'], strict_slashes=False)
def user_id():
    """returns the id of the current login user"""
    if current_user.is_authenticated:
        user = {"user_id": current_user.get_id()}
        print(current_user.get_id())
        return jsonify(user)
    else:
        print("No")
        return jsonify({"message": "User not authenticated"}), 401


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles login"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = next((user for user in storage.all(User).values() if user.email == email), None)
        if user and user.check_password(password):
            login_user(user)
            print("Session Data:", session)
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401



@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrive all users"""
    all_users = storage.all(User).values()
    user_list = []
    if not all_users:
        abort(404)
    for user in all_users:
        user_list.append(user.to_dict())
    return jsonify(user_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a user given an id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/county/<county_id>/users', methods=['GET'], strict_slashes=False)
def get_users_for_county(county_id):
    """Get users related to a specific county"""
    users = storage.all(User).values()
    user_list = []
    if not users:
        abort(404)
    for user in users:
        if user.county_id == county_id:
            user_list.append(user.to_dict())
    return jsonify(user_list)

@app_views.route('/town/<town_id>/users', methods=['GET'], strict_slashes=False)
def get_user_for_town(town_id):
    """Get all users for a specific town"""
    users = [user.to_dict() for user in storage.all(User).values() if user.town_id == town_id]
    if not users:
        abort(404)
    return jsonify(users)

@app_views.route('users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user given a user_id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/county/<county_id>/town/<town_id>/users',
        methods=['POST'], strict_slashes=False)
def create_user(county_id, town_id):
    """creates a new user with a county and town"""
    county = storage.get(County, county_id)
    town = storage.get(Town, town_id)

    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.county_id = county.id
    instance.town_id = town.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/county/<county_id>/users', methods=['POST'],
    strict_slashes=False)
def creates_user(county_id):
    """Creates a user given only a county"""
    county = storage.get(County, county_id)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")
    data = request.get_json()
    instance = User(**data)
    instance.county_id = county.id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def updates_user(user_id):
    """Updates a user"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    avoid = ['id', 'email', 'created_at', 'updated_at']
    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)


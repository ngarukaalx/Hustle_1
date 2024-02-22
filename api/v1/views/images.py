#!/usr/bin/python3
"""Holds all RESTAPI for image"""
from models import storage
from models.image import Image
from models.business import Business
from models.county import County
from models.town import Town
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/images', methods=['GET'], strict_slashes=False)
def get_images():
    """get all images and their related business and location"""
    all_images = storage.all(Image).values()
    sorted_images = sorted(all_images, key=lambda x: x.created_at, reverse=True)
    image_data = []
    for image in sorted_images:
        image_dict = image.to_dict()
        business_id = image_dict.get("business_id")
        business = storage.get(Business, business_id).to_dict()
        county_id = business.get("county_id")
        town_id = business.get("town_id")
        county = storage.get(County, county_id).to_dict()
        town = storage.get(Town, town_id).to_dict()
        image_dict.update({'town_location': town.get("name"),
                'county_location': county.get("name"),
                'business_name': business.get("name"),
                })
        image_data.append(image_dict)
    return jsonify(image_data)


@app_views.route('/images/<image_id>', methods=['GET'], strict_slashes=False)
def get_image(image_id):
    """Retrive image by id"""
    image = storage.get(Image, image_id)
    if not image:
        abort(404)
    return jsonify(image.to_dict())


@app_views.route('/image', methods=['GET'], strict_slashes=False)
def get_all_images():
    """Retrive all images"""
    all_images = storage.all(Image).values()
    list_images = []
    for image in all_images:
        list_images.append(image.to_dict())
    return jsonify(list_images)


@app_views.route('/images/<image_id>', methods=['DELETE'], strict_slashes=False)
def delete_image(image_id):
    """delete an image"""
    image = storage.get(Image, image_id)
    if not image:
        abort(404)
    storage.delete(image)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/business/<business_id>/images', methods=['POST'], strict_slashes=False)
def create_image(business_id):
    """Create an image"""
    if not request.get_json():
        abort(400, description="Not a JSON")
    if 'url' not in request.get_json():
        abort(400, description="Missing url")
    data = request.get_json()
    instance = Image(**data)
    instance.business_id = business_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('images/<image_id>', methods=['PUT'], strict_slashes=False)
def update_image(image_id):
    """Update an image"""
    image = storage.get(Image, image_id)
    if not image:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    avoid = ['id', 'created_at', 'updated_at', 'business_id']
    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(image, key, value)
    storage.save()
    return make_response(jsonify(image.to_dict()), 200)

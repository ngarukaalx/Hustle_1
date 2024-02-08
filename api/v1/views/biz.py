#!/usr/bin/python3
"""Holds the RESTAPI of business entity"""
from models import storage
from models.business import Business
from models.county import County
from models.town import Town
from models.video import Video
from models.image import Image
from models.logo import Logo
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from operator import itemgetter

@app_views.route('/biz', methods=['GET'], strict_slashes=False)
def get_biz():
    """Retrives a business with all of its information
    -video
    -image
    -logo # not yet implemented
    """
    all_business = storage.all(Business).values()
    business_data = []
    for business in all_business:
        business_data_dict = business.to_dict()
        business_id = business_data_dict.get("id")
        county_id = business_data_dict.get("county_id")
        town_id = business_data_dict.get("town_id")
        # get the county associated with the business
        county_instance = storage.get(County, county_id).to_dict()
        # get the county associated with the business
        town_insatnce = storage.get(Town, town_id).to_dict()
        # get the county name
        county_name = county_instance.get("name")
        # get the town name
        town_name = town_insatnce.get("name")
        business_videos = sorted([video.to_dict() for video in storage.all(Video).values() if video.business_id == business_id], key=itemgetter('created_at'), reverse=True)
        business_images = sorted([image.to_dict() for image in storage.all(Image).values() if image.business_id == business_id], key=itemgetter('created_at'), reverse=True)
        image_urls = [image["url"] for image in business_images]
        business_logo_object = [logo.to_dict() for logo in storage.all(Logo).values() if logo.business_id == business_id]
        video_urls = [video["url"] for video in business_videos]
        logo_url = business_logo_object[0]["url"] if business_logo_object else []

        business_data_dict.update({'business_videos': video_urls,
            'business_images': image_urls,
            'logo': logo_url,
            'county_name': county_name,
            'town_name': town_name
            })
        business_data.append(business_data_dict)
    return jsonify(business_data)

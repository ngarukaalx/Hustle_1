#!/usr/bin/python3
"""Holds all RESTAPI for video"""
from models import storage
from models.video import Video
from models.business import Business
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request

@app_views.route('/videos', methods=['GET'], strict_slashes=False)
def get_videos():
    """Retrive all videos"""
    all_videos = [video.to_dict() for video in storage.all(Video).values()]
    return jsonify(all_videos)


@app_views.route('/videos/<video_id>', methods=['GET'], strict_slashes=False)
def get_video(video_id):
    """Retrive video by id"""
    video = storage.get(Video, video_id)
    if not video:
        abort(404)
    return jsonify(video.to_dict())

@app_views.route('/businesses/<business_id>/videos', methods=['GET'], strict_slashes=False)
def get_video_for_business(business_id):
    """Get a video  associated with a business"""
    videos = [video.to_dict() for video in storage.all(Video).values() if video.business_id == business_id]
    if not videos:
        abort(404)
    return jsonify(videos)


@app_views.route('/videos/<video_id>', methods=['DELETE'], strict_slashes=False)
def delete_video(video_id):
    """Deletes a video"""
    video = storage.get(Video, video_id)
    if not video:
        abort(404)
    storage.delete(video)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/business/<business_id>/videos', methods=['POST'], strict_slashes=False)
def creates_video(business_id):
    """Creates a video"""
    if 'videoFile' not in request.files:
        abort(404, description="Not video file provides")
    vide_file = request.files['videoFile']
    video_description = request.form.get('description', '')

    if video_file.filename == "":
        abort(400, description="Empty video file name")
    # save the video file to the specified derectory
    video_path = f"hustle/uploads/videos/{business_id}_{secure_filename(video_file.filename)}"
    vide_file.save(video_path)
    # create a video instance and save it to the database
    video_data = {
            'url': video_path,
            'description': video_description,
            }
    instance = Video(**video_data)
    instance.business_id = business_id
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/videos/<video_id>', methods=['PUT'], strict_slashes=False)
def updates_video(video_id):
    """Updates a video"""
    video = storage.get(Video, video_id)
    if not video:
        abort(404)
    avoid = ['id', 'created_at', 'updated_at', 'business_id']
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in avoid:
            setattr(video, key, value)
    storage.save()
    return make_response(jsonify(video.to_dict()), 200)


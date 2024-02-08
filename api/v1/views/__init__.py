#!/usr/bin/python3
"""Blueprint for API"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.counties import *
from api.v1.views.towns import *
from api.v1.views.users import *
from api.v1.views.businesses import *
from api.v1.views.images import *
from api.v1.views.categories import *
from api.v1.views.videos import *
from api.v1.views.biz import *
from api.v1.views.logos import *

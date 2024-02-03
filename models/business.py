#!/usr/bin/python3
"""business class"""

import models
from models.base_model import BaseModel, Base
from models.video import Video
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Business(BaseModel, Base):
    """Representation of a business"""
    if models.storage_t == 'db':
        __tablename__ = 'businesses'
        name = Column(String(128), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        owner = relationship("User", back_populates="businesses")
        videos = relationship("Video", back_populates="business_videos", cascade="all, delete, delete-orphan")
        images = relationship("Image", back_populates="business_images", cascade="all, delete, delete-orphan")
        town_id = Column(String(60), ForeignKey('towns.id'), nullable=True)
        town = relationship("Town", backref="businesses_town")
        county_id = Column(String(60), ForeignKey('counties.id'), nullable=False)
        county = relationship("County", backref="businesses_county")
        description = Column(String(255), nullable=True)
        exact_location = Column(String(200), nullable=True)
    else:
        name = ""
        user_id = ""
        description = ""
        exact_location = ""

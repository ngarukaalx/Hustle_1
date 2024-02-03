#!/usr/bin/python3
"""Holds the video class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Video(BaseModel, Base):
    """representaion of a video class"""
    if models.storage_t == 'db':
        __tablename__ = 'videos'
        business_id = Column(String(60), ForeignKey('businesses.id'), nullable=False)
        business_videos = relationship("Business", back_populates="videos")
        url = Column(String(255), nullable=False)
        description = Column(String(255), nullable=True)
    else:
        business_id = ""
        url = ""
        description = ""

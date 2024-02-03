#!/usr/bin/python3
"""Holds the image class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Image(BaseModel, Base):
    """representaion of an image class"""
    if models.storage_t == 'db':
        __tablename__ = 'images'
        business_id = Column(String(60), ForeignKey('businesses.id'), nullable=False)
        business_images = relationship("Business", back_populates="images")
        url = Column(String(255), nullable=False)
        description = Column(String(255), nullable=True)
    else:
        business_id = ""
        url = ""
        description = ""

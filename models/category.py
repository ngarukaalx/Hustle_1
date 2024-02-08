#!/usr/bin/python3
"""Holds the category class"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class Category(BaseModel, Base):
    """Representation of a category"""
    if models.storage_t == 'db':
        __tablename__ = 'categories'
        name = Column(String(128), nullable=False, unique=True)
        businesses = relationship("Business", backref="category", cascade="all, delete, delete-orphan")
    else:
        name = ""
    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)

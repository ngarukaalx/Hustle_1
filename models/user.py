#!/usr/bin/python3
"""the user class"""


import models
from models.base_model import BaseModel, Base
from models.town import Town
from models.business import Business
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        town_id = Column(String(60), ForeignKey('towns.id'), nullable=False)
        # Establish a relationship with business
        businesses = relationship("Business", back_populates="owner", cascade="all, delete, delete-orphan")
        # Establish a relationship with town
        town = relationship("Town", backref="users")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

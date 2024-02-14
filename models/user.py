#!/usr/bin/python3
"""the user class"""


import models
from models.base_model import BaseModel, Base
from models.town import Town
from models.business import Business
from models.county import County
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from hashlib import md5
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """Representation of a user"""
    if models.storage_t == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        town_id = Column(String(60), ForeignKey('towns.id'), nullable=True)
        county_id = Column(String(60), ForeignKey('counties.id'), nullable=False)
        # Establish a relationship with county
        county = relationship("County", backref="users")
        # Establish a relationship with business
        businesses = relationship("Business", back_populates="owner", cascade="all, delete, delete-orphan")
        # Establish a relationship with town
        town = relationship("Town", backref="users")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)


    def __setattr__(self, name, value):
        """sets a password with md5 encription"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)

    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return self.password == md5(password.encode()).hexdigest()


    def is_active(self):
        """"Returns true if the user is active (non-disabled)"""
        return True


    def get_id(self):
        """Return the unique identifier for the user (unicode or str)"""
        return str(self.id)

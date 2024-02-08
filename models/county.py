#!/usr/bin/python3
"""class county"""

import models
from models.base_model import BaseModel, Base
from models.town import Town
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class County(BaseModel, Base):
    """Representation of county"""
    if models.storage_t == "db":
        __tablename__ = 'counties'
        name = Column(String(128), nullable=False, unique=True)
        towns = relationship("Town", backref="county", cascade="all, delete, delete-orphan")
    else:
        name = ""


    def __init__(self, *args, **Kwargs):
        """initializes county"""
        super().__init__(*args, **Kwargs)

    if models.storage_t != "db":
        @property
        def towns(self):
            """getter for list of towns instances related to the county"""
            town_list = []
            all_towns = models.storage.all(Town)
            for town in all_towns.values():
                if town.county_id == self.id:
                    town_list.append(town)
            return town_list

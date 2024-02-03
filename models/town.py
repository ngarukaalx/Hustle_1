#!/usr/bin/python3
"""holds the town class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Town(BaseModel, Base):
    """Representation of town"""
    if models.storage_t == "db":
        __tablename__ = 'towns'
        county_id = Column(String(60), ForeignKey('counties.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        county_id = ""
        name = ""

    def __init__(self, *args, **Kwargs):
        """initializes town"""
        super().__init__(*args, **Kwargs)

#!/usr/bin/python3
"""Holds the logo class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Logo(BaseModel, Base):
    """representaion of an logo class"""
    if models.storage_t == 'db':
        __tablename__ = 'logos'
        business_id = Column(String(60), ForeignKey('businesses.id'), nullable=False)
        business_logo = relationship("Business", back_populates="logo")
        url = Column(String(255), nullable=False)
    else:
        business_id = ""
        url = ""

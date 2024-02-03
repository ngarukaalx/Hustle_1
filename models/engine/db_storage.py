#!/usr/bin/python3
"""
Database storage engine
"""

import models
from models.base_model import BaseModel, Base
from models.county import County
from models.town import Town
from models.business import Business
from models.video import Video
from models.image import Image
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"BaseModel": BaseModel, "User": User, "County": County,
        "Town": Town, "Business": Business, "Video": Video, "Image": Image}

class DBStorage:
    """class for interaction with database"""

    __engine = None
    __session = None

    def __init__(self):
        """instantiate a DbStorage object"""
        HSTL_MYSQL_USER = getenv('HSTL_MYSQL_USER')
        HSTL_MYSQL_PWD = getenv('HSTL_MYSQL_PWD')
        HSTL_MYSQL_HOST = getenv('HSTL_MYSQL_HOST')
        HSTL_MYSQL_DB = getenv('HSTL_MYSQL_DB')
        HSTL_ENV = getenv('HSTL_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HSTL_MYSQL_USER,
            HSTL_MYSQL_PWD,
            HSTL_MYSQL_HOST,
            HSTL_MYSQL_DB
            ),
            pool_pre_ping=True
            )
        if HSTL_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database
        cretes the current database session"""

        Base.metadata.create_all(self.__engine)
        session_factoty = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factoty)
        self.__session = session



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
from models.category import Category
from models.logo import Logo
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"County": County, "User": User,
        "Town": Town, "Business": Business, "Video": Video, "Image": Image, "Category": Category, "Logo": Logo}

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

    def close(self):
        """call remove on session"""
        self.__session.remove()

    def reload(self):
        """reloads data from the database
        cretes the current database session"""

        Base.metadata.create_all(self.__engine)
        session_factoty = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(session_factoty)
        self.__session = session

    def get(self, cls, id):
        """A method to retrive one object"""
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clsa in all_class:
                count += len(models.storage.all(clsa).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

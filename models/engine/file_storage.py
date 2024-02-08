#!/usr/bin/python3
"""this module contains class FileStorage
"""


import json
import models
from models.base_model import BaseModel
from models.user import User
classes = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """serializes instances to a JSON file and deserializes
    """

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}


    def all(self, cls=None):
        """returns the dictionary of __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        try:
            with open(self.__file_path, 'r') as f:
                j_son = json.load(f)
            for key in j_son:
                self.__objects[key] = classes[j_son[key]["__class__"]](**j_son[key])
        except:
            pass

    def get(self, cls, id):
        """A method to retrive one object"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls-None):
        """Count the number objects in storage"""
        all_class = classes.values()
        if not cls:
            count = 0
            for clsa in all_class:
                count += len(models.storage.all(clsa).values())
        else:
            count = len(models.storage.all(cls).values())
        return count


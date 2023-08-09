#!/usr/bin/python3
"""cls serializes instances to a JSON file and deserializes JSON file"""
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
        cls serializes instances to a JSON file and deserializes
        JSON file to instances
        Args:
            file_path: path to the JSON file
            objects: will store all objects by <class name>.id
    """
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """ all(self): returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
           new(self, obj):
           sets in __objects the obj with key <obj class name>.id
           Args:
               obj: object passed
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """save(self):serializes __objects to the JSON file"""
        to_json = ""
        dict1 = {}
        for key, obj in self.__objects.items():
            dict1[key] = obj.to_dict()
        to_json = json.dumps(dict1)
        with open(self.__file_path, "w") as f:
            f.write(to_json)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dict1 = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dict1 = json.loads(f.read())
            """ convert dict to obj and insert them in __objects """
            for key, obj_dict in dict1.items():
                cls = globals()[obj_dict['__class__']]
                self.__objects[key] = cls(**obj_dict)

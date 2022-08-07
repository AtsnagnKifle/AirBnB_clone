#!/usr/bin/python3
"""
    A storage moudle.
"""
import json


class FileStorage:
    """
        A class that serializes instances to a JSON file and deserilaizes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            return the dictionary __objects
        """
        return __class__.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        __class__.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        dict_objs = {}
        for key in __class__.__objects:
            dict_objs[key] = __class__.__objects[key].to_dict()
        with open(__class__.__file_path, "w") as wr:
            json.dump(dict_objs, wr)

    def reload(self):
        """
            deserializes the JSON file to __objects. only if the
            JSON file (__file_path) exists otherwise, do nothing.
            If the file doesn’t exist, no exception raised
        """
        try:
            with open(__class__.__file_path) as rd:
                from models.base_model import BaseModel
                dict_objs = json.load(rd)
                for key in dict_objs:
                    if key.split(".")[0] == 'BaseModel':
                        __class__.__objects[key] = BaseModel(**dict_objs[key])

        except FileNotFoundError:
            pass

#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
"""file_storage module defines a class FileStorage that
serializes instances to a JSON file and deserializes
JSON file to instances with Private class attributes
file_path and objects and Public instance methods
all, new, save, reload.
"""


class FileStorage:
    """defines a class used for serialization of instances to JSON
    and deserialization of JSON to instances
    """
    __filepath = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        my_dict = {}
        for k, v in FileStorage.__objects.items():
            my_dict[k] = v.to_dict()
        with open(FileStorage.__filepath, "w") as f:
            f.write(json.dumps(my_dict))

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        my_dict = {}
        if os.path.exists(FileStorage.__filepath):
            with open(FileStorage.__filepath, "r") as f:
                my_dict = json.loads(f.read())
                for v in my_dict.values():
                    class_name = v['__class__']
                    del v['__class__']
                    self.new(eval(class_name)(**v))

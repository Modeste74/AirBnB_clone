#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        js_objs = {}
        for key, value in self.__objects.items():
            js_objs[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(js_objs, f)

    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, "r") as filename:
                json_data = json.load(filename)
            for key, value in json_data.items():
                cls_name, obj_id = key.split(".")
                if cls_name == "BaseModel":
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass

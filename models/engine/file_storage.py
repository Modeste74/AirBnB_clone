#!/usr/bin/python3

import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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
                    cls = BaseModel(**value)
                elif cls_name == "User":
                    cls = User(**value)
                elif cls_name == "Place":
                    cls = Place(**value)
                elif cls_name == "State":
                    cls = State(**value)
                elif cls_name == "City":
                    cls = City(**value)
                elif cls_name == "Amenity":
                    cls = Amenity(**value)
                elif cls_name == "Review":
                    cls = Review(**value)
                else:
                    continue
                self.__objects[key] = cls
        except FileNotFoundError:
            pass

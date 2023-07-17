#!/usr/bin/python3
"""defines a class BaseModel"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """defines a class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initializes the class attributes"""
        from models.__init__ import storage
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string rep of
        the BaseModel class
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the updated_at
        and ensures storage happens
        everytime an instance is created
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing the
        key and value of an instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

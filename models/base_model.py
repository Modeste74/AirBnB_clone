#!/usr/bin/python3
"""defines a class BaseModel"""

import uuid
from datetime import datetime

"""formated_time = specific_datetime.strftime("%Y-%m-%d %H:%M:%S:%f")"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

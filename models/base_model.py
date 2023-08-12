#!/usr/bin/python3
"""cls BaseModel defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ __init__(self): instantiate instance """
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                setattr(self, key, value)

                if key in ["created_at", "updated_at"] and\
                        isinstance(value, str):
                    setattr(self, key, datetime.fromisoformat(value))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ __str__(self): string representation of the class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            save(self): updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
           to_dict(self): returns a dictionary containing all keys/values of
           __dict__ of the instance
        """
        dict1 = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            dict1[key] = value
        dict1['__class__'] = self.__class__.__name__
        return dict1

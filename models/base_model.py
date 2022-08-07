#!/usr/bin/python3
"""
    defines all common attributes for other classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """
        Base Class
    """

    def __init__(self):
        """
            Base model constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """
            formated string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            update public instance attribute updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
        """
        my_dict = {
            "__class__": self.__class__.__name__
        }
        my_dict.update(self.__dict__)

        if "created_at" in my_dict:
            my_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in my_dict:
            my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

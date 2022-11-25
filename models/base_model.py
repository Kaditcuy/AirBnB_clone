#!/usr/bin/env python3

"""
Module containing BaseModel that defines all common attributes/methods
for other classes.
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Base model that defines all common
    attributes for other classes.
    """
    def __init__(self, *args, **kwargs):
        """Public attributes to initialze a BaseModel object with.

        Args:
            id (str): Holds UUID for eaach object created.
            created_at: Date and time for when an instance/object is created.
            updated_at: Date and time when an instance/object is created and this
                        attribute will be updated everytime you chnage your object.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
            prints a string representation of BaseModel instance
        """
        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates the public instance attribute updated_at with
            the current datetime.
        """
        self.updated_at = datetime.today()

	def to_dict(self):
        """
            returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict

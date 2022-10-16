#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from uuid import uuid4
import os
from datetime import datetime


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    def __init__(self, id=None, created_at=0, updated_at=0):
        """Constructor of Base Model
        """
        curr_time = datetime.now()
        self.id = str(uuid4())
        self.created_at = curr_time
        self.updated_at = curr_time

    def __str__(self):
        """Returns a string representation of BaseModel
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save the new changes with the actual time
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Representation in a dictionary of an instance
        """
        rep = dict(self.__dict__)
        rep["__class__"] = self.__class__.__name__
        rep["created_at"] = rep["created_at"].isoformat()
        rep["updated_at"] = rep["updated_at"].isoformat()
        return (rep)

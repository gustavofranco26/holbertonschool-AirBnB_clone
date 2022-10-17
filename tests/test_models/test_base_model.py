#!/usr/bin/python3

""" Module to test BaseModel """


from models.base_model import BaseModel
import unittest
import models
import os
from datetime import datetime
import json


class test_basemodel(unittest.TestCase):
    """ Test BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_save(self):
        """ Testing save
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_todict(self):
        """ Test todict
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_id(self):
        """ Test Id
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test Created_at
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime)

    def test_str(self):
        """ Test str representation
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

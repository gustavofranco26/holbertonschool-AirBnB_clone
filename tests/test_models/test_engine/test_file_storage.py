#!/usr/bin/python3

""" Module to test FileStorage """


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import models
import os
from models import storage


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method
    """
    def test_new(self):
        """ New object is correctly added to __objects
        """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
            self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned
        """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_save(self):
        """ FileStorage save method
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects
        """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_type_path(self):
        """ Confirm __file_path is string
        """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict
        """
        self.assertEqual(type(storage.all()), dict)

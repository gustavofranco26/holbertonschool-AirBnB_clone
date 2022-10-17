#!/usr/bin/python3
""" Testin City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Testing City """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Testing ID """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Testing name """
        new = self.value()
        self.assertEqual(type(new.name), str)

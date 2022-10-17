#!/usr/bin/python3
""" Testing State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test State"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

#!/usr/bin/python3
""" Module for testing state """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Class to test the state method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Testing name3 """
        new = self.value(**{"name": 'gkcjfgk'})
        self.assertEqual(type(new.name), str)

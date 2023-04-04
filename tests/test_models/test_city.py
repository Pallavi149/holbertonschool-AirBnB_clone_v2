#!/usr/bin/python3
""" Module for testing city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Class to test the city method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Testing state id """
        new = self.value(**{"state_id": "9wkwieo"})
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Testing name """
        new = self.value(**{"name": "eiww9k"})
        self.assertEqual(type(new.name), str)

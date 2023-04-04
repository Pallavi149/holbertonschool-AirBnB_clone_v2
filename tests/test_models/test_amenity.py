#!/usr/bin/python3
""" Module for testing amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Class to test the Amenity method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ function """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Testing name2 """
        new = self.value()
        self.assertEqual(type(new.name), str)

#!/usr/bin/python3
""" Module for testing place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ Class to test the place method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Testing city id """
        new = self.value(**{"city_id": "eiw[]"})
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Testing user id """
        new = self.value(**{"user_id": "389302ikewdd2"})
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ Testing name """
        new = self.value(**{"name": "9k3kspkmj"})
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ Testing description """
        new = self.value(**{"description": "uewokw0"})
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Testing number rooms """
        new = self.value(**{"number_rooms": 39})
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Testing number bathrooms """
        new = self.value(**{"number_bathrooms": 100})
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Testing max guest """
        new = self.value(**{"max_guest": 0})
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Testing price by night """
        new = self.value(**{"price_by_night": 9738})
        self.assertEqual(type(new.price_by_night), int)

    def test_longitude(self):
        """ Testing longitude """
        new = self.value(**{"latitude": 673.00})
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Testing amenity ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

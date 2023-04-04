#!/usr/bin/python3
""" Module for testing review """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Class to test the review method """

    def __init__(self, *args, **kwargs):
        """ Define __init__ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Testing place id """
        new = self.value(**{"place_id": '9eok2iko'})
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Testing user id """
        new = self.value(**{"user_id": "2iduwp"})
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ Testing text """
        new = self.value(**{"text": "ojdue9w0"})
        self.assertEqual(type(new.text), str)

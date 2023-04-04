#!/usr/bin/python3
""" Module for testing user """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ Class to test the basemodel """

    def __init__(self, *args, **kwargs):
        """ Define __init__ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Testing first name """
        new = self.value()
        new = self.value(**{"first_name": "Tom"})
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Testing last name """
        new = self.value()
        new = self.value(**{"last_name": "Jerry"})
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ Testing email """
        new = self.value()
        new = self.value(**{"email": "holbertschool@gmail.com"})
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Testing password """
        new = self.value()
        new = self.value(**{"password": "passwd"})
        self.assertEqual(type(new.password), str)

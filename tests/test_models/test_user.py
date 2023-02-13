#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
import models


class Test_User(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_useremail(self):
        self.assertTrue(type(self.user.email) is str)

    def test_userpassword(self):
        self.assertTrue(type(self.user.password) is str)

    def test_first_name(self):
        self.assertTrue(type(self.user.first_name) is str)

    def test_last_name(self):
        self.assertTrue(type(self.user.last_name) is str)

    def test_issubclass(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_to_dict(self):
        self.assertTrue(type(self.user.to_dict()) is dict)

    def test_useraddedtoobjects(self):
        self.assertIn(self.user, models.storage.all().values())

    def tearDown(self):
        self.user = None


if __name__ == "__main__":
    unittest.main()

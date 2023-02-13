#!/usr/bin/python3
import unittest
import models
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_name(self):
        self.assertTrue(type(self.city.name) is str)

    def test_state_id(self):
        self.assertTrue(type(self.city.state_id) is str)

    def test_issubclass(self):
        self.assertTrue(issubclass(City, BaseModel))

    def tearDown(self):
        self.city = None


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_name(self):
        self.assertTrue(type(self.amenity.name) is str)

    def test_subclass(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_to_dict(self):
        self.assertTrue(type(self.amenity.to_dict()) is dict)

    def test_instance_added_to_objects(self):
        self.assertIn(self.amenity, models.storage.all().values())

    def test_id(self):
        self.assertTrue(type(self.amenity.id) is str)

    def tearDown(self):
        self.amenity = None


if __name__ == "__main__":
    unittest.main()

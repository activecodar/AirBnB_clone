#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel


class Test_Place(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_city_id(self):
        self.assertTrue(type(self.place.city_id) is str)

    def test_user_id(self):
        self.assertTrue(type(self.place.user_id) is str)

    def test_name(self):
        self.assertTrue(type(self.place.name) is str)

    def test_description(self):
        self.assertTrue(type(self.place.description) is str)

    def test_number_rooms(self):
        self.assertTrue(type(self.place.number_rooms) is int)

    def test_number_bathrooms(self):
        self.assertTrue(type(self.place.number_bathrooms) is int)

    def test_max_guest(self):
        self.assertTrue(type(self.place.max_guest) is int)

    def test_price_by_night(self):
        self.assertTrue(type(self.place.price_by_night) is int)

    def test_latitude(self):
        self.assertTrue(type(self.place.latitude) is float)

    def test_longitude(self):
        self.assertTrue(type(self.place.longitude) is float)

    def test_amenity_ids(self):
        self.assertTrue(type(self.place.amenity_ids) is list)

    def test_issubclass(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def tearDown(self):
        self.place = None


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class Test_Review(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_place_id(self):
        self.assertTrue(type(self.review.place_id) is str)

    def test_user_id(self):
        self.assertTrue(type(self.review.user_id) is str)

    def test_text(self):
        self.assertTrue(type(self.review.text) is str)

    def test_issubclass(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def tearDown(self):
        self.review = None


if __name__ == "__main__":
    unittest.main()

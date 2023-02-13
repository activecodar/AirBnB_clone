#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class Test_State(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_name(self):
        self.assertTrue(type(self.state.name) is str)

    def test_issubclass(self):
        self.assertTrue(issubclass(State, BaseModel))

    def tearDown(self):
        self.state = None


if __name__ == "__main__":
    unittest.main()

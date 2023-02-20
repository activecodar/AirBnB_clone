#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime
import models
from time import sleep


class Test_BaseModel(unittest.TestCase):

    def test_uniqueInstanceId(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_instantiation_with_no_dict(self):
        b1 = BaseModel()
        self.assertEqual(BaseModel, type(b1))

    def test_id_is_string(self):
        b1 = BaseModel()
        self.assertTrue(type(b1.id) is str)

    def test_updated_at_is_datetimeObject(self):
        b1 = BaseModel()
        self.assertTrue(type(b1.updated_at) is datetime.datetime)

    def test_created_at_is_datetimeObject(self):
        b1 = BaseModel()
        self.assertTrue(type(b1.created_at) is datetime.datetime)

    def test_created_at_not_equal_to_updated_at(self):
        b1 = BaseModel()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_created_at_different_two_instances(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_new_instance_added_to_objects(self):
        b1 = BaseModel()
        self.assertIn(b1, models.storage.all().values())

    def test_updated_at_different_two_instances(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_instantiationwithDict(self):
        b1 = BaseModel()
        model_dict = b1.to_dict()
        b2 = BaseModel(**model_dict)
        self.assertTrue(type(b2) is BaseModel)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.updated_at, b2.updated_at)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1, b2)

    def test_instantiationWithEmptyDict(self):
        b1 = BaseModel(**{})
        self.assertTrue(type(b1) is BaseModel)
        self.assertTrue(type(b1.updated_at) is datetime.datetime)
        self.assertTrue(type(b1.created_at) is datetime.datetime)
        self.assertTrue(type(b1.id) is str)

    def test_to_dictfunction(self):
        b1 = BaseModel()
        b1.name = "Airbnb"
        base_dict = b1.to_dict()
        self.assertTrue(type(base_dict) is dict)
        self.assertTrue(base_dict['id'])
        self.assertTrue(base_dict['updated_at'])
        self.assertTrue(base_dict['created_at'])
        self.assertEqual(base_dict['__class__'], "BaseModel")
        self.assertEqual(base_dict['name'], "Airbnb")

    def test_savefunction(self):
        b1 = BaseModel()
        time = b1.updated_at
        b1.name = "python"
        b1.save()
        self.assertNotEqual(time, b1.updated_at)

    def test__str__(self):
        b1 = BaseModel()
        self.assertEqual(BaseModel.__str__(b1), "[{}] ({}) {}"
                         .format(type(b1).__name__, b1.id, b1.__dict__))


if __name__ == "__main__":
    unittest.main()

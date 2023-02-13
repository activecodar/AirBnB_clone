#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os
import models


class Test_FileStorage(unittest.TestCase):

    def setUp(self):
        self.b1 = BaseModel()

    def test_initialization(self):
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")
        self.assertTrue(type(models.storage.all()) is dict)

    def test_file_path(self):
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

    def test_objects_dict(self):
        self.assertTrue(type(models.storage._FileStorage__objects) is dict)

    def test_all(self):
        self.assertIn(self.b1, models.storage.all().values())

    def test_save(self):
        self.b1.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))
        with open(models.storage._FileStorage__file_path, "r") as f:
            my_dict = json.loads(f.read())
        self.assertIn(self.b1.to_dict(), my_dict.values())

    def test_reload_withoutJsonFile(self):
        models.storage.save()
        os.remove(models.storage._FileStorage__file_path)
        models.storage._FileStorage__objects = {}
        models.storage.reload()
        self.assertEqual(models.storage._FileStorage__objects, {})

    def test_reload_withJsonFile(self):
        models.storage._FileStorage__objects = {}
        models.storage.reload()
        self.assertIn(self.b1, models.storage.all().values())

    def test_reload(self):
        models.storage._FileStorage__objects = {}
        models.storage.reload()
        self.assertIn(self.b1, models.storage.all().values())

    def test_save_two_objects(self):
        b1 = BaseModel()
        b2 = BaseModel()
        b1.save()
        b2.save()
        with open(models.storage._FileStorage__file_path, "r") as f:
            my_dict = json.loads(f.read())
        self.assertIn(b1.to_dict(), my_dict.values())
        self.assertIn(b2.to_dict(), my_dict.values())

    def tearDown(self):
        self.b1 = None

if __name__ == "__main__":
    unittest.main()

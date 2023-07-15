#!/usr/bin/python3
"""defines unittest for the
class BaseModel"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import inspect
from unittest import mock
import models
import json
from models import storage

class TestBaseModel(unittest.TestCase):
    """tests for various functionality"""
    def setUp(self):
        self.base_model = BaseModel()

    def test_id(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"], self.base_model.updated_at.isoformat())
    
class TestBaseModel_storage(unittest.TestCase):
    base_model = BaseModel()
    def test_storage_new(self):
        instances_before = len(storage.all())
        base_model = BaseModel()
        self.base_model.save()
        instances_after = len(storage.all())
        self.assertGreater(instances_after, instances_before)

    def test_storage_save(self):
        self.base_model.save()
        storage_file_path = storage._FileStorage__file_path
        with open(storage_file_path, "r") as f:
            file_data = json.load(f)
            key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
            self.assertIn(key, file_data)

    def test_storage_reload(self):
        self.base_model.save()
        storage = FileStorage()
        storage.reload()
        instances = storage.all()
        key = "{}.{}".format(self.base_model.__class__.__name__, self.base_model.id)
        self.assertIn(key, instances)

"""class TestBaseErrors(unittest.TestCase):
    base_model = BaseModel()
    def test_invalid_attributes(self):
        with self.assertRaises(TypeError):
            self.base_model.id = 10
        with self.assertRaises(TypeError):
            self.base_model.created_at = "2023-07-14"
        with self.assertRaises(TypeError):
            self.base_model.updated_at = 100

    def test_missing_attributes(self):
        with self.assertRaises(AttributeError):
            _ = self.base_model.invalid_attribute"""


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""defines unittest for the
class BaseModel"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import inspect
from unittest import mock
import models


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



if __name__ == '__main__':
    unittest.main()

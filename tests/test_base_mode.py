#!/usr/bin/python3
"""
    test for base model
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        test for base model
    """

    def test_init(self):
        """
            test BaseModel public attribute
        """

        my_model = BaseModel()
        self.assertTrue(type(my_model.id), int)
        self.assertTrue(len(my_model.id), 36)
        self.assertTrue(type(my_model.updated_at), datetime)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

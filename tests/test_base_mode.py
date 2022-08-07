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

    def test_updated_time(self):
        """
            check if updated time is changed when new attrbutes created and the
            save function is called.
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_model.created_at)

    def test_str_representaion(self):
        """
            string representaion test.
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        self.assertEqual(str(my_model),
                         '[{}] ({}) {}'.format(my_model.__class__.__name__,
                                               my_model.id,
                                               my_model.__dict__))

    def test_kwargs(self):
        """
            test kwargs
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(str(my_model), str(my_new_model))
        self.assertFalse(my_model is my_new_model)


if __name__ == '__main__':
    unittest.main()

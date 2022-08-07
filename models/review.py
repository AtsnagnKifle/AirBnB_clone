#!/usr/bin/python3
"""
    Review class inherits BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        class Review
    """
    place_id = ""
    user_id = ""
    text = ""

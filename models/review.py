#!/usr/bin/python3
"""defines a subclass"""
from models.base_model import BaseModel


class Review(BaseModel):
    """reps the Review subclass"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """intializes the cleass
        review"""
        super().__init__(*args, **kwargs)

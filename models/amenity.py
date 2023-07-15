#!/usr/bin/python3
"""Module containing the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that reprs an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes new instance of the Amenity class."""
        super().__init__(*args, **kwargs)

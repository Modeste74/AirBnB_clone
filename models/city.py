#!/usr/bin/python3
"""
Module defining City class,
representing a city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Class that represents a city,
    inherits from BaseModel.
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of city class"""
        super().__init__(*args, **kwargs)

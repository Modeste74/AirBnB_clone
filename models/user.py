#!/usr/bin/python3
"""Module contains User class,
representing a user in the hbnb system.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class repr a user in hbnb,
    inherits from BaseModel class.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of user class.
        """
        super().__init__(*args, **kwargs)

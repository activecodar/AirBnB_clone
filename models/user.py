#!/usr/bin/python3
"""
The `user` module contains the implementation of the `User` class.
This class is a subclass of `BaseModel` from the `models.base_model`
module and represents a user in a housing system.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The `User` class is a subclass of `BaseModel` and represents a
    user in a housing system. It has two attributes:
    - `email`, a string that stores the email of the user
    - `password`, a string that stores the password of the user
    - `first_name`, a string that stores the first name of the user
    - `last_name`, a string that stores the last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

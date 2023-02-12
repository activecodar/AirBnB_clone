from models.base_model import BaseModel

"""
The `city` module contains the implementation of the `City` class.
This class is a subclass of `BaseModel` from the `models.base_model`
module and represents a city in a housing system.
"""


class City(BaseModel):
    """The `City` class is a subclass of `BaseModel` and represents a
    city in a housing system. It has two attributes:
    - `name`, a string that stores the name of the city
    - `state_id`, a string that stores the ID of the state that the
    city belongs to.
    """
    name = ""
    state_id = ""

from models.base_model import BaseModel

"""
The `amenity` module contains the implementation of the `Amenity` class.
This class is a subclass of `BaseModel` from the `models.base_model`
module and represents an amenity in a housing system.
"""


class Amenity(BaseModel):
    """
    The `Amenity` class is a subclass of `BaseModel` and represents an
    amenity in a housing system. It has a single attribute:
    - `name`: string that stores the name of the amenity.
    """
    name = ""

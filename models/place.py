from models.base_model import BaseModel

"""The `place` module contains the implementation of the `Place` class.
This class is a subclass of  `BaseModel` from the `models.base_model`
module and represents a place in a housing system.
"""


class Place(BaseModel):
    """The `Place` class is a subclass of `BaseModel` and represents
    a place in a housing system.
    It has several attributes:
    - `city_id`, a string that stores the ID of the city that the
       place belongs to.
    - `user_id`, a string that stores the ID of the user who owns
       the place.
    - `name`, a string that stores the name of the place.
    - `description`, a string that stores a description of the place.
    - `number_rooms`, an integer that stores the number of rooms in
       the place.
    - `number_bathrooms`, an integer that stores the number of bathrooms
       in the place.
    - `max_guest`, an integer that stores the maximum number of guests that
       the place can accommodate.
    - `price_by_night`, an integer that stores the price per night for staying
       in the place.
    - `latitude`, a float that stores the latitude coordinate of the place.
    - `longitude`, a float that stores the longitude coordinate of the place.
    - `amenity_ids`, a list of strings that stores the IDs of the amenities
       that are available in the place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

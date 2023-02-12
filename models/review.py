from models.base_model import BaseModel

"""The `review` module contains the implementation of the
`Review` class. This class is a subclass of
`BaseModel` from the `models.base_model` module and
represents a review in a housing system.
"""


class Review(BaseModel):
    """The `Review` class is a subclass of `BaseModel` and represents
    a review in a housing system. It has three attributes:
        - `place_id`, a string that stores the ID of the place
           that the review is about.
        - `user_id`, a string that stores the ID of the user
           who wrote the review.
        - `text`, a string that stores the text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""

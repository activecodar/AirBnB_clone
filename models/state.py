from models.base_model import BaseModel

"""The `state` module contains the implementation of the `State` class.
This class is a subclass of `BaseModel` from the `models.base_model`
module and represents a state in a housing system.
"""


class State(BaseModel):
    """The `State` class is a subclass of `BaseModel` and represents
    a state in a housing system. It has a single attribute:
    - `name`: a string that stores the name of the state.
    """
    name = ""

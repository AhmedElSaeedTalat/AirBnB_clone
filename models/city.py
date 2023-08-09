#!/user/bin/python3
""" city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class city inherits from BaseModel
        Args:
            state_id: string - empty string: it will be the State.id
            name: string - empty string
    """
    state_id = ""
    name = ""

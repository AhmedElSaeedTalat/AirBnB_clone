#!/user/bin/python3
""" aminity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class aminity inherits from BaseModel
        Args:
            name: string - empty string
    """
    name = ""

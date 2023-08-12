#!/usr/bin/python3
""" Write a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class intherits from BaseModel
        Args:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

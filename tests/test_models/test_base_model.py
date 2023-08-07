#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
import models.base_model
import inspect
import datetime


class TestBaseModel(unittest.TestCase):
    """ class to test base class """
    def setUp(self):
        self.b = BaseModel()

    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(BaseModel.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.base_model.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init(self):
        """ test instantiation of class """
        self.assertEqual(type(self.b.id), str)
        self.assertEqual(type(self.b.updated_at), datetime.datetime)
        self.assertEqual(type(self.b.created_at), datetime.datetime)

    def test_save(self):
        """ test BaseModel.save() """
        current_updatedAt = self.b.updated_at
        self.b.save()
        self.assertNotEqual(current_updatedAt, self.b.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.b.save(13)

    def test_to_dict(self):
        """ test BaseModel.to_dict() """
        self.b.name = "My First Model"
        self.b.my_number = 89
        dict1 = self.b.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['my_number']), int)
        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], 'BaseModel')
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.b.to_dict('str')

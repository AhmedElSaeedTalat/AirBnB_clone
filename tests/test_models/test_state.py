#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.state import State
import models.base_model
import models.state
import inspect
import datetime
from time import sleep


class TestState(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.s = State()

    def test_doc_state(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(State.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.state.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(State, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_state(self):
        """ test instantiation of class """
        self.assertEqual(type(self.s.id), str)
        self.assertEqual(type(self.s.updated_at), datetime.datetime)
        self.assertEqual(type(self.s.created_at), datetime.datetime)

    def test_save_state(self):
        """ test State.save() """
        current_updatedAt = self.s.updated_at
        self.s.save()
        self.assertNotEqual(current_updatedAt, self.s.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.s.save(13)

    def test_to_dict_state(self):
        """ test State.to_dict() """
        self.s.name = "NYC"
        dict1 = self.s.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "State")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.s.to_dict('str')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.city import City
import models.base_model
import models.city
import inspect
import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.c = City()

    def test_doc_city(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(City.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.city.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(City, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_city(self):
        """ test instantiation of class """
        self.assertEqual(type(self.c.id), str)
        self.assertEqual(type(self.c.updated_at), datetime.datetime)
        self.assertEqual(type(self.c.created_at), datetime.datetime)

    def test_save_city(self):
        """ test State.save() """
        current_updatedAt = self.c.updated_at
        self.c.save()
        self.assertNotEqual(current_updatedAt, self.c.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.save(13)

    def test_to_dict_city(self):
        """ test City.to_dict() """
        self.c.name = "NYC"
        dict1 = self.c.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "City")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.to_dict('str')


if __name__ == '__main__':
    unittest.main()

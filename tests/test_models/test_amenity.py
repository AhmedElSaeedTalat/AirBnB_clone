#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models.base_model
import models.amenity
import inspect
import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    """ class to test city class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.c = Amenity()

    def test_doc_amenity(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(Amenity.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.amenity.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(Amenity, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_init_amenity(self):
        """ test instantiation of class """
        self.assertEqual(type(self.c.id), str)
        self.assertEqual(type(self.c.updated_at), datetime.datetime)
        self.assertEqual(type(self.c.created_at), datetime.datetime)

    def test_save_amenity(self):
        """ test Amenity.save() """
        current_updatedAt = self.c.updated_at
        self.c.save()
        self.assertNotEqual(current_updatedAt, self.c.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.save(13)

    def test_to_dict_amenity(self):
        """ test Amenity.to_dict() """
        self.c.name = "NYC"
        dict1 = self.c.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['name']), str)
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "Amenity")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.to_dict('str')


if __name__ == '__main__':
    unittest.main()

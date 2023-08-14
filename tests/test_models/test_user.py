#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
from models.user import User
import models.base_model
import models.user
import inspect
import datetime
from time import sleep


class TestUser(unittest.TestCase):
    """ class to test user class """
    def setUp(self):
        """This method is called before each test method in the test class.
        """
        self.c = User()

    def test_doc_user(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(User.__doc__, 'no docs for Base class')
        self.assertIsNotNone(models.user.__doc__, 'no docs for module')
        for name, method in inspect.getmembers(User, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def check_attributes(self):
        """ check for attributes """
        user = User()
        user.first_name = "Jonas"
        user.last_name = "stones"
        user.email = "jonas@email.com"
        user.password = "root"
        self.assertEqual(user.first_name, "Jonas")
        self.assertEqual(user.last_name, "stones")
        self.assertEqual(user.email, "jonas@email.com")
        self.assertEqual(user.password, "root")
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "email"))
        self.assertEqual(type(User.email), str)
        self.assertEqual(type(User.first_name), str)
        self.assertEqual(type(User.last_name), str)
        self.assertEqual(type(User.password), str)

    def test_init_user(self):
        """ test instantiation of class """
        self.assertEqual(type(self.c.id), str)
        self.assertEqual(type(self.c.updated_at), datetime.datetime)
        self.assertEqual(type(self.c.created_at), datetime.datetime)

    def test_save_user(self):
        """ test User.save() """
        current_updatedAt = self.c.updated_at
        self.c.save()
        self.assertNotEqual(current_updatedAt, self.c.updated_at)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.save(13)

    def test_to_dict_city(self):
        """ test User.to_dict() """
        self.c.first_name = "jonas"
        self.c.last_name = "stones"
        self.c.email = "jonas@example.com"
        self.c.password = "root"
        dict1 = self.c.to_dict()

        """ confirming the type of each attr in dict """
        self.assertEqual(type(dict1['first_name']), str)
        self.assertEqual(dict1['first_name'], "jonas")
        self.assertEqual(dict1['last_name'], "stones")
        self.assertEqual(dict1['email'], "jonas@example.com")
        self.assertEqual(dict1['password'], "root")
        self.assertEqual(type(dict1['__class__']), str)
        self.assertEqual(dict1['__class__'], "User")
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['id']), str)
        self.assertEqual(type(dict1['created_at']), str)

        """ test positional args """
        with self.assertRaises(TypeError):
            self.c.to_dict('str')


if __name__ == '__main__':
    unittest.main()

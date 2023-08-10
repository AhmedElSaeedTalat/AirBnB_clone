#!/usr/bin/python3
# test cases for base class
import unittest
from models.base_model import BaseModel
import models.base_model
import inspect
import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ class to test base class """

    def setUp(self):
        """This method is called before each test method in the test class.
        """
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

        """Unittests for task 4
        """

    def test_model_from_dict(self):
        """test instantiation from a dictionary
        """
        # Example dictionary with attribute values
        instance_dict = {
            '__class__': "BaseModel",
            'id': '123',
            'created_at': '2023-08-07T15:30:51.120683',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }
        test_instance = BaseModel(**instance_dict)
        self.assertNotIn("__class__", test_instance.__dict__)
        self.assertEqual(type(test_instance.id), str)
        self.assertEqual(type(test_instance.created_at), datetime.datetime)
        self.assertEqual(type(test_instance.updated_at), datetime.datetime)
        self.assertEqual(type(test_instance.name), str)
        self.assertEqual(type(test_instance.my_number), int)

    def init_with_invalid_dates(self):
        """Test initialization with invalid date strings
        """
        # Example dictionary with attribute values
        invalid_dict = {
            'id': '123',
            'created_at': '2021-08-07T15:30:51.120690',
            'updated_at': '2023-08-07T15:30:51.120690',
            'name': 'julien',
            'my_number': 42
        }
        # Set invalid date string for created_at
        invalid_dict['created_at'] = "INVALID DATE"
        with self.assertRaises(ValueError):
            inst = BaseModel(**invalid_dict)

        # set invalid updated at:
        invalid_dict['updated_at'] = 2023
        with self.assertRaises(TypeError):
            inst = BaseModel(**invalid_dict)

    def test_str(self):
        """Testing __str__ method"""
        self.b.id = "1234"
        strForm = self.b.__str__()
        expected = "[BaseModel] (1234)"
        self.assertIn(expected, strForm)

    def test_save_updatedAt(self):
        """test updating the public instance attribute updated_at
            with the current datetime"""
        new_inst = BaseModel()  # create sleep update
        sleep(0.05)
        beforeSave_updated_at = new_inst.updated_at
        new_inst.save()
        self.assertLess(beforeSave_updated_at, new_inst.updated_at)


if __name__ == '__main__':
    unittest.main()

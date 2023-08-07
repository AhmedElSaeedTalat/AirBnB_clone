#!/usr/bin/python3
""" test file storage module """
import unittest
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel
import inspect
import os


class TestFileStorage(unittest.TestCase):
    """ test file storage class """
    def test_doc(self):
        """ test_doc(self): to test if module and class has docs """
        self.assertIsNotNone(FileStorage.__doc__, 'no docs for FileStorage')
        self.assertIsNotNone(models.engine.file_storage.__doc__, 'no docs')
        for name, method in inspect.getmembers(BaseModel, inspect.isfunction):
            self.assertIsNotNone(method.__doc__, f"{name} has no docs")

    def test_save_reload(self):
        """ test save(), reload(), all() functions """
        my_model = BaseModel()
        my_model.save()
        storage = FileStorage()
        """ check if file is created """
        self.assertTrue(os.path.exists('file.json'))

        """ load json file and check if objects are returned"""
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertEqual(type(obj), BaseModel)

        """ adding positional args """
        with self.assertRaises(TypeError):
            my_model.save('str')
        with self.assertRaises(TypeError):
            storage.reload('str')
        with self.assertRaises(TypeError):
            storage.all('str')


if __name__ == "__main__":
    unittest.main()

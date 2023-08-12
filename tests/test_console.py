#!/usr/bin/python3
""" test console """
import unittest
import inspect
from console import HBNBCommand
import console
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json


class TestConsole(unittest.TestCase):
    """ test console """

    def test_doc_console(self):
        """ test_doc_console(self): to test if module and class has docs """
        self.assertIsNotNone(HBNBCommand.__doc__, 'no docs for Base class')
        self.assertIsNotNone(console.__doc__, 'no docs for module')

    def test_quit_EOF(self):
        """ test quit and EOF functions in cmd """
        self.assertEqual(HBNBCommand().onecmd("EOF"), True)
        self.assertEqual(HBNBCommand().onecmd("quit"), True)

    def test_empty_line(self):
        """ Test handling empty lines """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual("", output.getvalue())


class TestCreate(unittest.TestCase):
    """Test Creating a new instance of Class,
    saves it (to the JSON file)"""

    def test_args_length(self):
        """test if args length < 1 to print [** class name missing **]"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_invalid_className(self):
        """Test if input is not a valid class"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create UnknownClass"
            expected = "** class doesn't exist **"
            HBNBCommand().onecmd(input)  # excute command
            self.assertEqual(expected, output.getvalue().strip())

    def test_create(self):
        """test creating a new instance of a Class,
        saves it (to the JSON file)"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create BaseModel"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "BaseModel.{}".format(captured_id)
            input = "create BaseModel"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create User"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "User.{}".format(captured_id)
            input = "create User"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Amenity"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Amenity.{}".format(captured_id)
            input = "create Amenity"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create State"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "State.{}".format(captured_id)
            input = "create State"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Place"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Place.{}".format(captured_id)
            input = "create Place"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create City"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "City.{}".format(captured_id)
            input = "create City"
            self.assertIn(inst_key, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            input = "create Review"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "Review.{}".format(captured_id)
            self.assertIn(inst_key, storage.all().keys())


class TestShow(unittest.TestCase):
    """ test show feature"""
    def test_show(self):
        """ test show """
        b = BaseModel()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'BaseModel.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[BaseModel] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = User()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'User.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[User] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = State()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'State.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[State] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = City()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'City.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[City] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = Place()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'Place.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[Place] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = Amenity()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'Amenity.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[Amenity] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

        b = Review()
        id = b.id
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'Review.show("{id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = f"[Review] ({id}) {b.__dict__}"
            self.assertEqual(output.getvalue().strip(), res)

    def test_errors(self):
        """ test passing invalid id """
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = "** no instance found **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing no class """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'show'
            HBNBCommand().onecmd(input)  # excute command
            res = "** class name missing **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing incorrect class """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'places.show("232342")'
            HBNBCommand().onecmd(input)  # excute command
            res = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing not passing id """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'Place.show()'
            HBNBCommand().onecmd(input)  # excute command
            res = "** instance id missing **"
            self.assertEqual(output.getvalue().strip(), res)


class TestCount(unittest.TestCase):
    """ test count """
    def test_count(self):
        """ test count function """
        count = 0
        for key, values in storage.all().items():
            name = key.split(".")
            if name[0] == 'BaseModel':
                count += 1
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'BaseModel.count()'
            HBNBCommand().onecmd(input)
            self.assertEqual(output.getvalue().strip(), str(count))


class TestAll(unittest.TestCase):
    """ test all funtion """
    def test_all(self):
        """test all function """
        b = BaseModel()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'BaseModel.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[BaseModel]")

        b = User()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'User.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[User]")

        b = State()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'State.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[State]")

        b = City()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'City.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[City]")

        b = Amenity()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'Amenity.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Amenity]")

        b = Place()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'Place.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Place]")

        b = Review()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'Review.all()'
            HBNBCommand().onecmd(input)
            list_obj = json.loads(output.getvalue())
            for obj in list_obj:
                obj = obj.split()
                self.assertEqual(obj[0], "[Review]")

    def test_invalidClass(self):
        """ test invalid calss """
        b = Review()
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'review.all()'
            HBNBCommand().onecmd(input)
            expected_output = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
""" test console """
import unittest
import inspect
from console import HBNBCommand
import console
from unittest.mock import patch
from io import StringIO


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


if __name__ == '__main__':
    unittest.main()

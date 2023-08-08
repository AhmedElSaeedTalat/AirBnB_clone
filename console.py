#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function to exit the cmd """
        return True

    def do_EOF(self, line):
        """ function to exit the cmd """
        print()
        return True

    def help_quit(self):
        """ help guide for quit command """
        print('Quit command to exit the program')

    def help_EOF(self):
        """ help guide for EOF command """
        print('EOF command to exit the program')

    def emptyline(self):
        """ handles empty lines """
        pass


if __name__ == '__main__':
    if not sys.stdin.isatty():
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()

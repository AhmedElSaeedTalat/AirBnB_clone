#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function to exit the cmd """
        return True

    def help_quit(self):
        """ help guide for quit command """
        self.stdout.write('Quit command to exit the program\n')

    def help_EOF(self):
        """ help guide for EOF command """
        self.stdout.write('EOF command to exit the program\n')

    def help_help(self):
        """ displays information about help guide """
        self.stdout.write("displays information about help guide\n")

    def emptyline(self):
        """ handles empty lines """
        pass

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()

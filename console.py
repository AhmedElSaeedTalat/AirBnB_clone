#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel
from models import storage


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        """
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name != "BaseModel" and \
                class_name != BaseModel().__class__.__name__:
            print("** class doesn't exist **")
            return

        new_inst = BaseModel()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """ Prints the string representation of
        an instance based on the class name and id
        Example: show BaseModel 49faff9a-6318-451f-87b6-910505c55907"""
        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("**instance id missing **")
            return

        class_name = args[0]
        cls = globals().get(class_name)  # Get the class by name
        id = args[1]

        if class_name != "BaseModel" and not issubclass(cls, BaseModel):
            print("** class doesn't exist **")
            return

        instances_dict = storage.all()  # get stores objects as dict
        id_list = []
        for key in instances_dict:
            # ex output:['BaseModel', '4f834043-3592-407b-8db5-08a22a06e9ab'] :
            class_name, inst_id = key.split(".")
            id_list.append(inst_id)

        if id in id_list:
            instance = instances_dict[f"{class_name}.{id}"]
            print(instance.__str__())
        else:
            print("** no instance found ** ")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""

        args = arg.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("**instance id missing **")
            return

        instances_dict = storage.all()  # get stores objects as dict
        if "{}.{}".format(args[0], args[1]) not in instances_dict.keys():
            print("** no instance found **")
        else:
            del instances_dict["{}.{}".format(args[0], args[1])]
            storage.save()


if __name__ == '__main__':
    if not sys.stdin.isatty():
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())
    else:
        HBNBCommand().cmdloop()

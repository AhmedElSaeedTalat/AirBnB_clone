#!/usr/bin/python3
""" the entry point of the command interpreter """
import cmd
import shlex
import sys
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

# remove object from class HBNBCommand(cmd.Cmd):


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    # dictionary of all classes
    all_classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    }
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ function to exit the cmd """
        return True
# quit and EOF to exit the program, no printing

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

# add do_help

    def do_help(self, line):
        """overrides help method"""
        cmd.Cmd.do_help(self, line)

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        """
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        else:
            cls = globals()[class_name]
            new_inst = cls()
            print(new_inst.id)
            storage.save()

    def do_show(self, arg):
        """ Prints the string representation of
        an instance based on the class name and id
        Example: show BaseModel 49faff9a-6318-451f-87b6-910505c55907"""
        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        cls = globals().get(class_name)  # Get the class by name
        id = args[1]

        if class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return

        instances_dict = storage.all()  # get stores objects as dict
        id_list = []
        """ check if instance exists and if yes it gets printed, otherwise
            no instance found would be printed
        """
        for key, obj in instances_dict.items():
            name = key.split(".")
            if obj.id == id and name[0] == class_name:
                try:
                    print(obj)
                    return
                except KeyError:
                    print("** no instance found **")

        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234."""

        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instances_dict = storage.all()  # get stores objects as dict
            del instances_dict["{}.{}".format(args[0], args[1])]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name.
        Ex: $ all BaseModel or $ all."""

        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return

        obj_list = []

        inst_dict = storage.all()
        for key in inst_dict:
            inst = inst_dict[key]

            if len(args) == 0 or (len(args) > 0 and
                                  args[0] == inst.__class__.__name__):
                obj_list.append(inst_dict[key].__str__())
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute
        (save the change into the JSON file).
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        valid_ids = []
        id = args[1]

        try:

            objects_dict = storage.all()
            for key in objects_dict:
                class_name, inst_id = key.split(".")
                valid_ids.append(inst_id)
                if id in valid_ids:
                    obj = objects_dict[f"{class_name}.{id}"]
                    attr = args[2]
                    value = args[3]
                    setattr(obj, attr, value)
                    storage.save()
                    return
            print("** no instance found **")
            return

        except KeyError:
            print("** no instance found **")

    def do_count(self, arg):
        """ count number of instances """
        count = 0
        class_name = arg
        all_instances = storage.all()
        for key, obj in all_instances.items():
            name = key.split(".")
            if name[0] == class_name:
                count += 1
        print(count)

    def default(self, arg):
        """ overwrite defauls behaviour for commands cls.method() """

        regex = re.match(r"(\w+\.\w+)(.*)", arg)
        list_command_args = ["do_show", "do_destroy"]

        """ to check if expression matches cls.method()
            example: User.all() if yes default method would
            be overritten accordingly """
        if regex:
            """ get class name and mehtod to call from passed string
                using match group and split function """
            grp1 = regex.group(1)
            grp1 = grp1.split(".")
            cls_name = grp1[0]
            method_name = grp1[1]
            full_method_name = "do_" + method_name
            method = getattr(self, full_method_name)
            if full_method_name in ["do_all", "do_count"]:
                method(cls_name)
            elif full_method_name in list_command_args:
                """ get id as it is needed for this list of commands
                    if not passed only class name is passed """
                regex1 = re.match(r'\(\"(.*)\"\)', regex.group(2))
                if regex1:
                    id = regex1.group(1)
                    method(f"{cls_name} {id}")
                else:
                    method(f"{cls_name}")
            elif full_method_name == "do_update":
                regex1 = re.findall(r'[\w\-\@\.]+', regex.group(2))
                if len(regex1) == 3:
                    args = " ".join(regex1)
                    method(f"{cls_name} {args}")
                elif len(regex1) > 3:
                    new_list = []
                    new_list.append(regex1[0])
                    for i, arg in enumerate(regex1):
                        if i == 0:
                            continue
                        new_list.append(arg)
                        if i % 2 == 0:
                            args = " ".join(new_list)
                            method(f"{cls_name} {args}")
                            new_list = []
                            new_list.append(regex1[0])

        else:
            return super().default(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()

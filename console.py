#!/usr/bin/python3
"""This module provides a command-line interface for the HBNB program."""

import re
import cmd
import sys
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage

"""classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Review": Review
        }"""


class HBNBCommand(cmd.Cmd):
    """
    Class representing hbnb command line interface,
    inherits from the cmd.Cmd class.
    """

    prompt = "(hbnb) " if sys.__stdin__.isatty() else ""

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Review": Review
        }

    valid_commands = ['all', 'count', 'show', 'destroy', 'update']

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Helper method for quit command"""
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """Method for exiting program"""
        return True

    def help_EOF(self):
        """Helper method for exit command"""
        print("Exit the hbnb program")

    def emptyline(self):
        """Execute nothing when an empty line is entered"""
        pass

    def precmd(self, line):
        """
        Hook method used to handle specific methods before
        execution of a command.
        """
        class_name = command = item_id = args = ''
        if not ('.' in line and '(' in line and ')' in line):
            return line
        try:
            parsed_line = line[:]
            class_name = parsed_line[:parsed_line.find('.')]
            command = parsed_line[parsed_line.find('.') + 1:parsed_line.find('(')]
            if command not in valid_commands:
                raise Exception
            parsed_line = parsed_line[parsed_line.find('(') + 1:parsed_line.find(')')]
            if parsed_line:
                parsed_line = parsed_line.partition(', ')
                item_id = parsed_line[0].replace('\"', '')
                parsed_line = parsed_line[2].strip()
                if parsed_line:
                    if parsed_line[0] == '{' and parsed_line[-1] == '}' and type(eval(parsed_line)) is dict:
                        args = parsed_line
                    else:
                        args = parsed_line.replace(',', '')
                        line = ' '.join([command, class_name, item_id, args])
        except Exception as error:
            pass
        finally:
            return line


    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_create(self, arg):
        """Creates new instance of specified class"""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split(" ")[0]
        if class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes[class_name]()
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """Prints help documentation for create"""
        print("Creates a new instance of a specified class\n")
        print("Usage: create <class_name>\n")

    def do_show(self, arg):
        """Displays details of specific instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if not instance_id:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def help_show(self):
        """Prints the help documentation for show"""
        print("Displays details of a specific instance\n")
        print("Usage: show <class_name> <instance_id>\n")

    def do_destroy(self, arg):
        """Deletes a specified instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        if not instance_id:
            print("** instance id missing **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        del storage.all()[key]
        del instance

    def help_destroy(self):
        """Prints help documentation for destroy"""
        print("Deletes a specific instance\n")
        print("Usage: destroy <class_name> <instance_id>\n")

    def do_all(self, arg):
        """Displays all instances/instances of a specified class."""
        if arg not in classes and arg != "":
            print("** class doesn't exist **")
            return
        print_list = []
        if arg:
            class_name = arg
            for key, value in storage.all().items():
                if class_name in key:
                    instance = value
                    print_list.append(str(instance))
            print(print_list)
        else:
            for key, value in storage.all().items():
                instance = value
                print_list.append(str(instance))
            print(print_list)

    def help_all(self):
        """Prints help documentation for all"""
        print("Displays all instances/instances of a specified class\n")
        print("Usage: all [<class_name>]\n")

    def do_count(self, arg):
        """Counts the num of instances of a specified class."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split(" ")[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        count = sum(
                1 for instance in storage.all().values()
                if isinstance(instance, classes[class_name])
                )
        print(count)

    def help_count(self):
        """Prints help documentation for count"""
        print("Counts the number of instances of a specified class\n")
        print("Usage: count <class_name>\n")

    def do_update(self, arg):
        """Updates the attribs of a specific instance."""

        args = arg.split()
        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        if not instance_id:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, instance_id)

        if key not in storage.all():
            print("no instance found **")
            return

        instance = storage.all()[key]

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = " ".join(args[3:]).strip('"')
        if not hasattr(instance, attribute_name):
            setattr(instance, attribute_name, "")
        attribute_type = type(getattr(instance, attribute_name))
        casted_value = attribute_type(attribute_value)
        setattr(instance, attribute_name, casted_value)
        instance.save()

    def help_update(self):
        """Prints the help documentation for update"""
        print("Updates the attrs of a specific instance\n")
        print("Usage: update <class_name> <instance_id> <attribute_name> "
              "<attribute_value>\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
"""if not sys.stdin.isatty():
    commands = sys.stdin.read().strip().split('\n')
    hbnb_cmd = HBNBCommand()
    hbnb_cmd.use_rawinput = False
    hbnb_cmd.intro = ""

    hbnb_cmd.prompt = "(hbnb) "

    for command in commands:
        print(hbnb_cmd.prompt)
        hbnb_cmd.onecmd(command)
        if hbnb_cmd.do_quit:
            break
    print(hbnb_cmd.prompt)
else:
    if __name__ == '__main__':
        HBNBCommand().cmdloop()"""

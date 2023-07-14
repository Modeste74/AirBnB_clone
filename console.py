#!/usr/bin/python3
import re
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models import storage

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
        "City": City, "State": State, "Amenity": Amenity,
        "Review": Review}
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        line = line.strip()
        components = line.split(".")
        if len(components) > 1:
            class_name, command = components[0], components[1]
            """class_name = class_name.capitalize()"""
            if class_name not in classes:
                print("** class doesn't exist **")
                return ""
            if command == "all()":
                return f"all {class_name}"
            if command == "count()":
                return f"count {class_name}"
            if command.startswith("show(") and command.endswith(")"):
                instance_id = re.search(r'"([^"]*)"', line).group(1)
                return f"show {class_name} {instance_id}"
            if command.startswith("destroy(") and command.endswith(")"):
                command = command[8:-1].strip()
                instance_id = re.search(r'"([^"]*)"', line).group(1)
                return f"destroy {class_name} {instance_id}"
            if command.startswith("update("):
                command = command[7:-1].strip()
                instance_id, updates_str = command.split(",", 1)
                instance_id = instance_id.strip(' "')
                updates = eval(updates_str.strip())
                attribute_updates = " ".join([f"{key} {value}" for key, value in updates.items()])
                return f"update {class_name} {instance_id} {attribute_updates}"

        return line

    def do_create(self, arg):
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
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split(" ")[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for instance in storage.all().values() if isinstance(instance, classes[class_name]))
        print(count)

    def help_count(self):
        """Prints help documentation for count"""
        print("Counts the number of instances of a specified class\n")
        print("Usage: count <class_name>\n")

    def do_update(self, arg):

        args = arg.split()
        """if len(args) < 3:
            print("Error")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("no instance found **")
            return
        instance = storage.all()[key]
        attribute_dict = eval("{" + " ".join(args[2:]) + "}")
        for attribute_name, attribute_value in attribute_dict.items():
            if not hasattr(instance, attribute_name):
                setattr(instance, attribute_name, "")
            attribute_type = type(getattr(instance, attribute_name))
            casted_value = attribute_type(attribute_value)
            setattr(instance, attribute_name, casted_value)
        instance.save()"""
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
        print("Usage: update <class_name> <instance_id> <attribute_name> <attribute_value>\n")



if not sys.stdin.isatty():
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
        HBNBCommand().cmdloop()

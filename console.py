#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage

classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
        "City": City, "State": State, "Amenity": Amenity,
        "Review": Review}
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """helper method for quit command"""
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

    def do_update(self, arg):

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

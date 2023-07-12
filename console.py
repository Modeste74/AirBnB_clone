#!/usr/bin/python3
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
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
if not sys.stdin.isatty():
    commands = sys.stdin.read().strip().split('\n')
    hbnb_cmd = HBNBCommand()
    hbnb_cmd.use_rawinput = False
    hbnb_cmd.intro = ""

    hbnb_cmd.prompt = "(hbnb) "

    for command in commands:
        hbnb_cmd.onecmd(command)
        if hbnb_cmd.do_quit:
            break

    if not hbnb_cmd.do_quit:
        hbnb_cmd.cmdloop(intro="")

else:
    if __name__ == '__main__':
        HBNBCommand().cmdloop()

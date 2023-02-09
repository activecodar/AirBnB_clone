#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

"""
Console entrypoint module for teh AirBnB console application.
"""


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB project,
    inheriting from the Cmd class.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Escpaes the command interpreter loop, technically closing the app.

        Args:
            line (str): The command line input.

        Returns:
            bool: Signal the end of the command interpreter loop.
        """
        return True

    def do_EOF(self, line):
        """
        Exits the command interpreter loop at EOF.

        Args:
            line (str): The terminal input.

        Returns:
            bool: Signal the end of the command interpreter loop.
        """
        print()
        return True

    def emptyline(self):
        """
        Executes nothing when on empty line.
        """
        pass

    def do_create(self, model):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Ex: $ create BaseModel

        Args:
            model (str): The class name from which to create an instance.
        """
        if model == "":
            print("** class name missing **")
        elif model != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self):
        """
        Prints the string representation of an instance based
        on the class name and id.
        
        Ex: $ show BaseModel 1234-1234-1234

        Args:
            model (str): The class name from which to create an instance.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

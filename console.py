#!/usr/bin/python3
import cmd

from models.utils import (get_classes, get_formatted_records,
                          classes_to_str_list)

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
        model_classes = get_classes()
        model_classes_lst = classes_to_str_list(model_classes)
        if model == "":
            print("** class name missing **")
        elif model not in model_classes_lst:
            print("** class doesn't exist **")
        else:
            model_instance = [i.get(model) for i in model_classes
                              if i.get(model) is not None][0]()
            model_instance.save()
            print(model_instance.id)

    def do_show(self, show_args):
        """
        Prints the string representation of an instance based
        on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234

        Args:
            show_args (str): The class name from which to create an instance.
        """
        model_classes = get_classes()
        model_classes_lst = classes_to_str_list(model_classes)
        if show_args == "":
            print("** class name missing **")
            return
        else:
            split_details = show_args.split()
            model = split_details[0]
            model_id = split_details[1] if len(split_details) > 1 else ""
            if model != "" and model not in model_classes_lst:
                print("** class doesn't exist **")
                return
            elif model_id == "" and model in model_classes_lst:
                print("** instance id missing **")
                return
            elif model in model_classes_lst and model_id != "":
                model_instance = [i.get(model) for i in model_classes
                                  if i.get(model) is not None][0]()
                response = model_instance.get_single_record(model_id)
                print(model_instance.__str__()) if response else None
                return

    def do_destroy(self, delete_args):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.

        Args:
            show_args (str): The class name from which to create an instance.
        """
        model_classes = get_classes()
        model_classes_lst = classes_to_str_list(model_classes)
        if delete_args == "":
            print("** class name missing **")
            return
        else:
            split_details = delete_args.split()
            model = split_details[0]
            model_id = split_details[1] if len(split_details) > 1 else ""
            if model != "" and model not in model_classes_lst:
                print("** class doesn't exist **")
                return
            elif model_id == "" and model in model_classes_lst:
                print("** instance id missing **")
                return
            elif model in model_classes_lst and model_id != "":
                model_instance = [i.get(model) for i in model_classes
                                  if i.get(model) is not None][0]()
                response = model_instance.delete_record(model_id)
                print(model_instance.__str__()) if response else None
                return

    def do_all(self, model_name):
        model_classes = get_classes()
        model_classes_lst = classes_to_str_list(model_classes)
        if model_name != "" and model_name not in model_classes_lst:
            print("** class doesn't exist **")
            return
        elif model_name == "":
            final_list = []
            for klass in model_classes:
                klass_name = [i for i in klass.keys()][0]
                final_list.extend(get_formatted_records(model_classes,
                                                        klass_name))
            print(final_list)
        else:
            results = get_formatted_records(model_classes, model_name)
            print(results)
            return

    def do_update(self, update_args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        model_classes = get_classes()
        model_classes_lst = classes_to_str_list(model_classes)
        if update_args == "":
            print("** class name missing **")
            return
        else:
            update_args = update_args.split()
            model_name = update_args[0]
            if model_name not in model_classes_lst:
                print("** class doesn't exist **")
                return
            elif len(update_args) == 1:
                print("** instance id missing **")
                return
            else:
                if len(update_args) < 3:
                    print("** attribute name missing **")
                    return
                elif len(update_args) < 4:
                    print("** value missing **")
                    return
                else:
                    model_name = update_args[0]
                    record_id = update_args[1]
                    attribute_name = update_args[2]
                    attribute_value = update_args[3]
                    model_inst = [i.get(model_name)
                                  for i in model_classes
                                  if i.get(model_name) is not None][0]()
                    record = model_inst.get_single_record(record_id)
                    if record is None:
                        return
                    model_inst.update_record(record=record,
                                             attr_name=attribute_name,
                                             attr_value=attribute_value)
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()

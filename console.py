#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model1 import BaseModel
import json
import models
import shlex
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """This class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    classes = {'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                           'Review'}

    def emptyline(self):
        """Ignores empty spaces
        """
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file
        """
        return True

    def do_create(self, arg):
        """Creates a new instance of the AirBNB class
        and saves it to a JSON file
        """
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
            pass
        elif args[0] in HBNBCommand.classes:
            new = eval(args[0])()
            print(new.id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance
           based on the class name and id
        """
        models.storage.reload()
        if len(arg) < 1:
            print("** class name missing **")
            pass
        else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print("** instance id missing **")
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                    print(FileStorage._FileStorage__objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if len(arg) < 1:
            print("** class name missing **")
            pass
        else:
            arg = arg.split(' ')
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print("** instance id missing **")
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                        FileStorage._FileStorage__objects.pop(key)
                        models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances
        based or not on the class name
        """
        models.storage.reload()
        if len(arg) < 1:
            all_items = []
            for value in FileStorage._FileStorage__objects.values():
                all_items.append(str(value))
            if not all_items:
                return
            print(all_items)
        else:
            arg = arg.split(" ")
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                all_items = []
                for value in FileStorage._FileStorage__objects.values():
                    if arg[0] in value.__class__.__name__:
                        all_items.append(str(value))
                if not all_items:
                    return
                print(all_items)

    def do_update(self, arg):
        """Updates an isntance based on the class name and id
        by adding or updating attribute (Save the change into
        the JSON file)
        Usage: update <class name> <id> <attribute> <value>
        id, created_at and updated_at cannot be updated
        """
        models.storage.reload()
        if len(arg) < 1:
            print("** class name missing **")
            pass
        else:
            arg = shlex.split(arg)
            if arg[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif arg[0] in HBNBCommand.classes:
                if len(arg) < 2:
                    print("** instance id missing **")
                    return
                key = arg[0] + '.' + arg[1]
                if key in FileStorage._FileStorage__objects:
                    dict_to_update = \
                        FileStorage._FileStorage__objects[key].__dict__
                    if len(arg) < 3:
                        print("** attribute name missing **")
                    elif len(arg) < 4:
                        print("** value missing **")
                    else:
                        k = arg[2]
                        try:
                            attrtype = type(dict_to_update[k])
                            v = attrtype(arg[3])
                        except KeyError:
                            v = arg[3]
                        dict_to_update[k] = v
                        models.storage.save()
                else:
                    print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

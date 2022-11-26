#!/usr/bin/env python3

"""
Module containing Command interpreter to manage AirBnB objects
"""

import cmd
import sys

class AirBnBShell(cmd.Cmd):
    """Command line interpreter"""
    intro = 'Welcome to the HBnb shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ ==  "__main__":
    AirBnBShell().cmdloop()

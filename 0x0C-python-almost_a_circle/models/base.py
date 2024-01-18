#!/usr/bin/python3
"""defining a base class."""

import json

class Base:
    """creating a class base."""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns he JSON representation list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json_string = json.dumps(list_dictionaries)

        return to_json_string


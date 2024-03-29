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

    @staticmethod
    def save_to_file(cls, list_objs):
        """
        Returns the JSON representation of list_objs.
        Args:
            list_objs (list): A list of instance who inherits of base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dic = []
                for obj in list_objs:
                    list_dic.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dic))
    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        Args:
            json_string  (str): A JSON string representing a list of dictionaries
        Returns:
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
           return []
        return json.loads(json_string)

    @staticmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)

            return dummy

    @staticmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        
        try:
            with open(filename, "r") as jsonfile:
               list_dicts = Base.from_json_string(jsonfile.read())

               list_instances = []

               for d in list_dicts:
                   list_instances.append(cls.create(**d))
               return list_instances
        except FileNotFoundError:
            return []


    
                        



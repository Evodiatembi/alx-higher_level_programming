#!/usr/bin/python3
"""representing a square class."""

from models.rectangle import Rectangle

class Square(Rectangle):
     """creating a class square from a rectangle class."""

     def __init__(self, size, x=0, y=0, id=None):
         """
         Class constructor for the square.
         """

         super().__init__(size, size, x, y, id)

     def __str__(self):
        """ overloading the str"""
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)


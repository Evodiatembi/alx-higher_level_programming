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

     @property
     def size(self):
        """get size of the square."""
        return self.width

     @size.setter
     def size(self, value):
        if not int: #check if width is not an integer
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

     def __str__(self):
        """ overloading the str"""
        return "[square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
     

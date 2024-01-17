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

     def update(self, *args, **kwargs):
        """
        assigning arguments to attributes.
    
        Args:
            *args (ints): attributes values.
                - 1st argument should be the id attribute
                - 2nd argument should be the size attribute
                - 3rd argument should be the x attribute
                - 4th argument should be the y attribute
            **kwargs (dict): new key/value pairs of attributes.
        """
        if args:
            for count, arg in enumerate(args):
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break




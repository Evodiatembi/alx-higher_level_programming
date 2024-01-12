#!/usr/bin/python3
"""representing a rectangle class."""

from models.base import Base

class Rectangle(Base):
    """creating a class rectangle from a base class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
         
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not int: #check if width is not an integer
            raise TypeError("width must be integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not int: #check if height is not an integer
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0: #check if x is less than 0
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0: #check if y is less than 0
            raise ValueError("y must be >= 0")
        self.__y = value


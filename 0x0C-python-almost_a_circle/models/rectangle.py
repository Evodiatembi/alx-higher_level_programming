#!/usr/bin/python3
"""representing a rectangle class."""

from models.base import Base

class Rectangle(Base):
    """creating a class rectangle from a base class."""
    def __init__(self, width, height, x=5, y=5, id=1):
        super().__init__(id=None)
         
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

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
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def area(self):
        """
        implementing a public method area that returns the area of the rectangle.
        """
        area = self.width * self.height
        return area

    def display(self):
        """
        implemnting a public method that print stdout with the character #
        """
        for i in range(self.x):
            print()
        for i in range(self.width):
            print(" " * self.y + "#" * self.height)

    def __str__(self):
        """
        implementing overriding the __str__ method.
        """
        return f"[Rectangle] ({self.id}) {self.x/self.y} - {self.width}/{self.height}"

    def update(self, *args):
        """
        assigning arguments to attributes 

        Args:
            *args (ints): New attribute values.
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        """
        if len(args) < 5:
            attributes = ["id", "width", "height", "x", "y"]
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
    def to_dictionary(self):
        """
        Returns the dictionary representation of the rectangle.
        """
        rect_dict = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
        }
        return rect_dict
               



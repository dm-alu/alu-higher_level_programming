#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Set the id, the size and the position of the rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def validate_integer(name, value, strictly_positive=False):
        """Check that a value is an integer and in the allowed range."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if strictly_positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not strictly_positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating it."""
        self.validate_integer("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating it."""
        self.validate_integer("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get the horizontal position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal position of the rectangle after validating it."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the vertical position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical position of the rectangle after validating it."""
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character # in stdout."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the description of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes with positional arguments or keyword arguments."""
        names = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name in names:
                if name in kwargs:
                    setattr(self, name, kwargs[name])

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

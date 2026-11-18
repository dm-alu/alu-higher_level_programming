#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Set the id, the size and the position of the square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height of the square to the same value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the description of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes with positional arguments or keyword arguments."""
        names = ("id", "size", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name in names:
                if name in kwargs:
                    setattr(self, name, kwargs[name])

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

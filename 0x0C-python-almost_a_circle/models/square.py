#!/usr/bin/python3
"""Definition of a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """This is a square"""

    def __init__(self, size, x=0, y=0):
        """Initialisation of a new Square

        Args:
            size: int
            x: int
            y: int
        """
        super().__init__(size, size, x, y, id)

        @property
        def size(self):
            """size getter"""
            return self.width

        @size.setter
        def size(self, value):
            """size setter"""
            self.width = value
            self.heigjt = value

        def __str__(self):
            """Updated representation of the Square"""
            return "[Square] ({}) {]/{} - {}".format(self.id, self.x, self.y,
                                                     self.width)

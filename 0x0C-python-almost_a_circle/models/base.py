#!usr/bin/python3
"""The Class Base module"""

class Base:
    """The Class: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id : int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
 

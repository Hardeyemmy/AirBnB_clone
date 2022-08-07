#!/usr/bin/python3
"""
New class base - code that pass pycodestyle test

"""
class Area:
    """ Defines an area """
    def __init__(self, length=0, breadth=0):
        if type(length) != int:
            raise TypeError("length must be intger")
        self.__length = length

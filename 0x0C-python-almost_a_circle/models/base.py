#!/usr/bin/python3

"""Defines a base model class"""


import csv
import json
import turtle


class Base:
    """Base model


    This represents the 'base' class for the entire project


    Private class attributes:
        __nb_objects (int): number of instantiated objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new base

        Args:
            id (int): identity of the new base

        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

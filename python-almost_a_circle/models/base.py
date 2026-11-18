#!/usr/bin/python3
"""Module that defines the Base class of the almost a circle project."""
import csv
import json
import os


class Base:
    """Base class that manages the id attribute of all its subclasses."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Set the id to the given value or to the next free number."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objects to a file."""
        if list_objs is None:
            list_objs = []
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance of the class with all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return the list of instances stored in the JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as a_file:
            dictionaries = cls.from_json_string(a_file.read())
        return [cls.create(**dictionary) for dictionary in dictionaries]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a list of objects to the CSV file of the class."""
        if list_objs is None:
            list_objs = []
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        with open(cls.__name__ + ".csv", "w", newline="") as a_file:
            writer = csv.writer(a_file)
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                writer.writerow([dictionary[name] for name in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return the list of instances stored in the CSV file."""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        else:
            fields = ["id", "size", "x", "y"]
        instances = []
        with open(filename, "r", newline="") as a_file:
            for row in csv.reader(a_file):
                if row:
                    values = [int(value) for value in row]
                    instances.append(cls.create(**dict(zip(fields, values))))
        return instances

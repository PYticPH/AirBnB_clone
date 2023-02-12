#!/usr/bin/python3

""" Storage engine for Airbnb:
> stores data in json format
> convert json object back to type dict
"""

import json
import os


class FileStorage:
    """ class object which defined storage of type json """

    __file_path = "db.json"
    __objects = {}

    def all(self):
        """ return object of type dict """
        return self.__objects

    def new(self, obj):
        """ create and set object data in dict __object """

        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serialize __object to path __file_path """

        tmp_db = {}

        with open(self.__file_path, "w") as data_db:
            for keys, values in self.__objects.items():
                tmp_db[keys] = values.to_dict()
                data = json.dump(tmp_db, data_db)

    def reload(self):
        """ Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception
        should be raised)"""

        if (os.path.exists(self.__file_path)):
            with open(self.__file_path, "r") as load_db:
                try:
                    self.__objects = json.load(load_db)
                except Exception as e:
                    pass

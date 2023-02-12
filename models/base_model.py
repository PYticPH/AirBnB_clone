#!/usr/bin/python3
""" A module to create a base model of Airbnb """
from models import storage
import uuid
import datetime


class BaseModel:
    """ Defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Generate UUID with time created """

        if kwargs:
            for k, v in kwargs.items():
                if (k != "__class__"):
                    if (k == "updated_at") | (k == "created_at"):
                        v = datetime.datetime.strptime(
                                v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def save(self):
        """ Update UUID creation time """

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of
        __dict__ of the instance """

        ins_dict = self.__dict__.copy()
        ins_dict['__class__'] = self.__class__.__name__
        ins_dict['id'] = self.id
        ins_dict['created_at'] = self.created_at.isoformat()
        if (self.updated_at):
            ins_dict['updated_at'] = self.updated_at.isoformat()
        return ins_dict

    def __str__(self):
        """ str representation of class BaseModel """

        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

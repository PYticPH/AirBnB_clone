#!/usr/bin/python3
""" basemodel test suite """

from models.base_model import BaseModel
import unittest
import uuid
import datetime

class TestBaseModel(unittest.TestCase):
    """ class BaseModel test casses """

    tc_a = BaseModel()
    tc_b = BaseModel()

    def test_save(self):
        """ Test save method on update_at attribute """
        self.assertEqual(tc_a.save(), tc_a.updated_at)

    def test_save_updated_at(self):
        """ Test updated_at """
        self.old_updated_at = tc_a.updated_at
        tc_a.save()
        self.assertNotEqual(self.old_updated_at, updated_at)

if __name__ == "__main__":
    unittest.main()

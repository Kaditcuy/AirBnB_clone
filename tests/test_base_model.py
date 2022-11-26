#!/usr/bin/env python3

"""
Module containing unittest for BaseModel
"""

import unittest
from models.base_model import BaseModel


class Test_BaseModel_instantiation(unittest.TestCase):
    """Tesing the creation/instantiation of the Basemodel class or its objects"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_i

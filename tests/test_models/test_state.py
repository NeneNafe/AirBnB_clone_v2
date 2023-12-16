#!/usr/bin/python3
"""this is a class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test for teststate class"""

    def __init__(self, *args, **kwargs):
        """init test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test for name 3"""
        new = self.value()
        self.assertEqual(type(new.name), str)

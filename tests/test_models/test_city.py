#!/usr/bin/python3
"""this is a class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """this is test for city model"""

    def __init__(self, *args, **kwargs):
        """init test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test for state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test for name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

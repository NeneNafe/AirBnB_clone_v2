#!/usr/bin/python3
"""this is a class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """test for place class"""

    def __init__(self, *args, **kwargs):
        """init class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test for class id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test for user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test for name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test for description"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test for number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test for max guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test for price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test for longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test for amenity"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

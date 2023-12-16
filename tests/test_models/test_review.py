#!/usr/bin/python3
"""class for tests"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """test review"""

    def __init__(self, *args, **kwargs):
        """this is the test for initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """place id test"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """user id test"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test text"""
        new = self.value()
        self.assertEqual(type(new.text), str)

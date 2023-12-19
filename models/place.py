#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from models import hbnb_storage
from sqlalchemy.orm import relationship
import models
from uuid import uuid4

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if hbnb_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

    def __init__(self, **kwargs):
        self.id = str(uuid4())
        for key, value in kwargs.items():
            setattr(self, key, value)

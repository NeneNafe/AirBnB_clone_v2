#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from models import hbnb_storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if hbnb_storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''

        @property
        def cities(self):
            """Returns City instances"""
            all_cities = models.storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]

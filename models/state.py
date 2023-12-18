#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """to initialise the state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns City instances"""
            val_cities = models.storage.all("City").values()
            city_list = []
            for city in val_cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

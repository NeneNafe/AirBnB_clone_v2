#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from models.city import City
from sqlalchemy.orm import relationship
from models import hbnb_storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """Returns City instances"""
        City_Class = BaseModel.all_classes('City')
        result = models.storage.all(City_Class)
        selected_city = [val for key, val in result.items()
                         if val.state_id == self.id]
        return selected_city
    if os.getenv('HBN_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref=backref('state'))

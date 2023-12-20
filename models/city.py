#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import hbnb_storage
from uuid import uuid4


class City(BaseModel, Base):
    """ The function represents a city """
    __tablename__ = 'cities'
    # if hbnb_storage == 'db':
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship(
        'Place', backref='cities',
        cascade='all, delete, delete-orphan', single_parent=True)
    cities = relationship(
        'City', backref='State', cascade='all, delete-orphan',
        single_parent=True
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.id = str(uuid4())
        # for key, value in kwargs.items():
        #     setattr(self, key, value)
    # else:
    #     name = ''
    #     state_id = ''
    @property
    def cities(self):
        """Returns City instances"""
        from models import storage
        from models.city import City
        all_cities = storage.all(City)
        return [city for city in all_cities.values()
                if city.state_id == self.id]

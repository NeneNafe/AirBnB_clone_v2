#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import hbnb_storage
from uuid import uuid4
from models.place import Place


class City(BaseModel, Base):
    """ The function represents a city """
    __tablename__ = 'cities'
    if hbnb_storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        places = relationship('Place', backref='city',
                              cascade='all, delete, delete-orphan')

        def __init__(self, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    else:
        name = ''
        state_id = ''
    
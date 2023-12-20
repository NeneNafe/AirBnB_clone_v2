#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # if hbnb_storage == 'db':
    name = Column(String(128), nullable=False)
    # else:
    #     name = ''

    cities = relationship(
            'City', backref='State', cascade='all, delete-orphan',
            single_parent=True
            )

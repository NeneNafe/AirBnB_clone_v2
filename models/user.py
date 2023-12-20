#!/usr/bin/python3
"""This module defines a class User"""
from uuid import uuid4
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import hbnb_storage
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if hbnb_storage == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship(
            'User', backref='places',
            cascade='all, delete, delete-orphan')
        places = relationship(
            'Place',
            backref='user', cascade='all, delete, delete-orphan',
            single_parent=True
            )

        def __init__(self, *args, **kwargs):
            self.id = str(uuid4())
            for key, value in kwargs.items():
                setattr(self, key, value)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

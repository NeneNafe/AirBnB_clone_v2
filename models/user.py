#!/usr/bin/python3
"""This module defines a class User"""
from uuid import uuid4
from models.base_model import BaseModel
from models.base_model import Base, Column, String
from models import hbnb_storage
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

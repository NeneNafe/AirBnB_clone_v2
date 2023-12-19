#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
import models
import os

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs == {}:
            return
        
        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.fromisoformat(value)
            if key != '__class__':
                self.__dict__[key] = value
        """Instatntiates a new model"""
        from models import storage
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        our_dict = self.__dict__.copy()
        our_dict['created_at'] = self.created_at.isoformat()
        our_dict['updated_at'] = self.updated_at.isoformat()
        our_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in our_dict.keys():
            del our_dict['_sa_instance_state']
        return our_dict

    def delete(self):
        """deletes the current instance from the storage"""
        models.storage.delete(self)

#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4
from datetime import datetime
import models
from models import hbnb_storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # self.created_at = datetime.now()
        # self.updated_at = datetime.now()
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            if 'created_at' in kwargs and 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            kwargs.pop('__class__', None)
            self.__dict__.update(kwargs)
            self.id = kwargs.get('id', str(uuid.uuid4()))
            

    def __str__(self):
        """str method
        Returns:
            class name, id and __dict__ representation
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.to_dict()}'

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    # def to_dict(self):
    #     """Convert instance into dict format"""
    #     our_dict = self.__dict__.copy()
    #     our_dict['created_at'] = self.created_at.isoformat()
    #     our_dict['updated_at'] = self.updated_at.isoformat()
    #     our_dict['__class__'] = self.__class__.__name__
    #     if '_sa_instance_state' in our_dict:
    #         del our_dict['_sa_instance_state']
    #     return our_dict
    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy.pop('_sa_instance_state', None)

        # Check if created_at is None, and set a default value
        created_at = getattr(self, 'created_at', None)
        if created_at:
            dict_copy['created_at'] = created_at.isoformat()

        # Handle the case where updated_at is None
        updated_at = getattr(self, 'updated_at', None)
        if updated_at:
            dict_copy['updated_at'] = updated_at.isoformat()

        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

    def delete(self):
        """this is the delete method"""
        from models import storage
        storage.delete(self)

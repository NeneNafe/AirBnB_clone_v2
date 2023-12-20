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
    id = Column(String(60), nullable=False,
                primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

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

    def __str__(self):
        """str method
        Returns:
            class name, id and __dict__ representation
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.to_dict()}'

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
    # def to_dict(self):
    #     """returns a dictionary containing all keys/values of the instance
    #     id
    #     created_at
    #     updated_at
    #     """
    #     # return {
    #     # "__class__": self.__class__.__name__,
    #     # "id": self.id,
    #     # "created_at": self.created_at.isoformat(),
    #     # "updated_at": self.updated_at.isoformat(),
    #     # }
    #     our_dict = self.__dict__.copy()
    #     our_dict["__class__"] = type(self).__name__
    #     our_dict["created_at"] = our_dict["created_at"].isoformat()
    #     our_dict["updated_at"] = our_dict["updated_at"].isoformat()
    #     return our_dict

    # def delete(self):
    #     """deletes the current instance from the storage"""
    #     models.storage.delete(self)

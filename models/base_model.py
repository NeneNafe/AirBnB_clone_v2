#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at
        if kwargs:
            for key in ["created_at", "updated_at"]:
                setattr(self, key, datetime.fromisoformat(value))
        elif key != "__class__":
            setattr(self, key, value)
        
            # self.id = str(uuid.uuid4())
            # self.created_at = datetime.utcnow()
            # self.updated_at = datetime.utcnow()
        #else:
        #    if 'created_at' in kwargs and 'updated_at' in kwargs:
         #      kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
          #                                              '%Y-%m-%dT%H:%M:%S.%f')
           #     kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
            #                                            '%Y-%m-%dT%H:%M:%S.%f')
            #kwargs.pop('__class__', None)
           # self.__dict__.update(kwargs)
            #self.id = kwargs.get('id', str(uuid.uuid4()))

    def __str__(self):
        """str method
        Returns:
            class name, id and __dict__ representation
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        my_dict = {}
        my_dict.update(self.to_dict())
        del my_dict["__class__"]
        return '[{}] ({}) {}'.format(cls, self,id, my_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        #from models import storage
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

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
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
            (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_as_instance_state' in dictionary.key():
            del dictionary['_as_instance_state']
        return dictionary

    def delete(self):
        """this is the delete method"""
        models.storage.delete(self)

    @classmethod
    def all_classes(cls, sub_cls=None):
        """return a dict of parent class and all subclasses"""
        classes = set([cls]).union(cls.__subclasses__())
        set_all = {c.__name__: c for c in classes}
        if sub_cls:
            return set_all[sub_cls]
        else:
            return set_all

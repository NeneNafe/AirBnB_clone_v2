#!/usr/bin/python3
"""The database storage class"""

import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_list = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """The new engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialises the objects"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """defines all the classes"""
        if not self.__session:
            self.reload()
        obj_list = {}
        if type(cls) == str:
            cls = class_list.get(cls, None)
        if cls:
            for objs in self.__session.query(cls):
                obj_list[objs.__class__.__name__ + '.' + objs.id] = objs
        else:
            for cls in class_list.values():
                for objects in self.__session.query(cls):
                    obj_list[objs.__class__.__name__ + '.' + objs.id] = objs
        return objs

    def new(self, obj):
        """Adds new object to the current db"""
        self.session.add(obj)

    def save(self):
        """commits all the changes of the curr db session"""
        self.session.commit()

    def delete(self, obj=None):
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Laods information in the database"""
        our_factory = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scooped_seassion(our_factory)

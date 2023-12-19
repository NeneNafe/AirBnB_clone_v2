#!/usr/bin/python3
"""The database storage class"""

from os import getenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The new engine class"""
    __engine = None
    __session = None
    class_list = [State, City, User, Amenity, Place, Review]

    def __init__(self):
        """Initialises the objects"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        db_url = f'mysql+mysqldb://{user}:{pwd}@{host}/{db}'

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """defines all the classes"""

        objcts_dict = {}

        if cls is None:
            for _class in self.class_list:
                list_of_objs = self.__session.query(_class).all()

                for obj in list_of_objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objcts_dict[key] = obj

            return objcts_dict

        cls = eval(cls) if type(cls) is str else cls
        if cls is not self.class_list:
            return None

        objct_list = self.__session.query(cls).all()
        for obj in objct_list:
            key = type(obj).__name__ + '.' + obj.id
            objcts_dict[key] = obj
        return self.dict_of_objects

    def new(self, obj):
        """Adds new object to the current db"""
        self.__session.add(obj)

    def save(self):
        """commits all the changes of the curr db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete objctes from the table"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Laods information in the database"""
        try:
            Base.metadata.create_all(self.__engine)
        except Exception:
            pass
        our_session = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(our_session)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()

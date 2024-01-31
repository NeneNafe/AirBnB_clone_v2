#!/usr/bin/python3
"""The database storage class"""

from sqlalchemy import create_engine
from sqlalchemy .orm import sessionmaker, scoped_session
from sqlalchemy import MetData, inspect
from models.base_model import BaseModel, Base
import os


class DBStorage:
    """The new engine class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the objects"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if env == 'test':
            metadata = MetaData()
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """defines all the classes"""

        classes = []
        if cls:
            classes.append(cls)
        else:
            for table in Base.metadata.tables:
                mapped_class = None
                for mapper in Base.registry.mappers:
                    if mapper.table[0].name == table:
                        mapped_class = mapper.class_
                        classes.append(mapped_class)
                        break

        dict_objects = {}
        for cls in classes:
            rows = self.__session.query(cls).all()
            for r in rows:
                class_name = r.__class__.__name__
                dict_objects.update({f"{class_name}.{r.id}": r})
        return dict_objects

    def new(self, obj):
        """Adds new object to the current db"""
        self.__session.add(obj)

    def save(self):
        """commits all the changes of the curr db session"""
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()

    def delete(self, obj=None):
        """Delete objects from the table"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads information in the database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        ses_factory = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        Session = scoped_session(ses_factory)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.remove()

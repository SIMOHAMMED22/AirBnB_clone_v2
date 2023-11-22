#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import Base

from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

username = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database_name = getenv("HBNB_MYSQL_DB")
environ = getenv("HBNB_ENV")


class DBStorage:
    """This class manages storage of hbnb models in mysql"""

    __session = None
    __engine = None

    def __init__(self):
        """create an engine"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, host, database_name), pool_pre_ping=True)

        if environ == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Query objects from the current database session."""
        # print('all func was called')
        if cls is None:
            objs = self.__session.query(User, State, City,
                                        Amenity, Place, Review).all()
        else:
            objs = self.__session.query(cls).all()
        dictionary = {}

        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """Add the object to the current database session."""
        # print('add obj to session')
        if obj not in self.__session:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()
        # print('save the changes')

    def delete(self, obj=None):
        """Delete obj from the current database session if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        from sqlalchemy import inspect
        """Create all tables and set up the current database session."""
        # print('create session')

        Base.metadata.create_all(self.__engine)
        # inspector = inspect(self.__engine)
        # table_names = inspector.get_table_names()
        # print("Tables created:", table_names)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

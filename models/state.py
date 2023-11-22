#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

type_storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'


    if type_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state",cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Return list of City with the current id instance"""
            from models import storage
            from models.city import City
            ls = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    ls.append(city)
            return ls
        name = ""

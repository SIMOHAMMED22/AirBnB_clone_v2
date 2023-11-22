#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

type_storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if type_storage == 'db':
        cities = relationship('City', backref="state",
                              cascade='all, delete-orphan')
    elif type_storage == 'file':
        def cities(self):
            """Return list of City with the current id instance"""
            from models import storage
            ls = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    ls.append(city)
            return ls
    # name = ""

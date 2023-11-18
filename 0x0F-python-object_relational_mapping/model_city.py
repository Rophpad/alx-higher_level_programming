#!/usr/bin/python3
"""  the class definition of a city
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Represents a city for a MySQL database

         __tablename__ (str): The name of the MySQL table to store States.
         id (int): The city's id.
         name (sqlalchemy.String): The city's name.
         state_id (sqlalchemy.Integer): The city's state id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

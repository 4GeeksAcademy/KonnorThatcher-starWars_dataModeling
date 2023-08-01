import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(30), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    gender = Column(String(10))
    birth_year = Column(String(20))
    species = Column(String(100))
    eye_color = Column(String(20))
    height = Column(Integer)
    weight = Column(Integer)
    homeworld = Column(String(200))
    created = Column(DateTime)
    edited = Column(DateTime)


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    terrain = Column(String(100))
    climate = Column(String(100))
    diameter = Column(Integer)
    hours_in_day = Column(Integer)
    days_in_year = Column(Integer)
    population = Column(Integer)
    created = Column(DateTime)
    edited = Column(DateTime)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    model = Column(String(100))
    starship_class = Column(String(100))
    length = Column(Integer)
    cargo_capacity = Column(Integer)
    speed_in_mglt = Column(Integer)
    crew_members = Column(Integer)
    passenger_capacity = Column(Integer)
    created = Column(DateTime)
    edited = Column(DateTime)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    starship_id = Column(Integer,ForeignKey('starship.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

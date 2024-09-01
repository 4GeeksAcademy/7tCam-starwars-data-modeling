import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship('Favorites', backref='user', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    hair_color = Column(String(250))
    eyes_color = Column(String(250))
    gender = Column(String(250))
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    favorites = relationship('Favorites', backref='characters', lazy=True)
    vehicles = relationship('Vehicles', backref='characters', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
    favorites = relationship('Favorites', backref='planets', lazy=True)
    characters = relationship('Characters', backref='planets', lazy=True)
    vehicles = relationship('Vehicles', backref='planets', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    favorites = relationship('Favorites', backref='vehicles', lazy=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

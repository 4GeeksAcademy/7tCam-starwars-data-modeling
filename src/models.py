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
    favoritesses = relationship('Favorites', backref='user', lazy=True)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     addresses = db.relationship('Address', backref='person', lazy=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    charactersses = relationship('Characters', backref='favorites', lazy=True)
    Planetsses = relationship('Planets', backref='favorites', lazy=True)
    vehiclesses = relationship('Vehicles', backref='favorites', lazy=True)


    # name_favorites = Column(String(250))

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name_characters = Column(String(250))
    hair_color = Column(String(250))
    eyes_color = Column(String(250))
    gender = Column(String(250))
    Favorites_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)

    # class Address(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(120), nullable=False)
    # person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
    #     nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name_planets = Column(String(250))
    population = Column(String(250))
    terrain = Column(String(250))
    Favorites_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name_vehicles = Column(String(250))
    Favorites_id = Column(Integer, ForeignKey('favorites.id'), nullable=False)

  
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    mail = Column(String(250), nullable=False)
    phone = Column(Integer, nullable=True)

    favourites = relationship('Favourite', back_populates='user')

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    name = "Favorites"
    id_user = Column(Integer, ForeignKey('user.id'))
    id_people = Column(Integer, ForeignKey('people.id'))
    id_planet = Column(Integer, ForeignKey('planet.id'))
    id_vehicle = Column(Integer, ForeignKey('vehicle.id'))
    id_starship = Column(Integer, ForeignKey('starship.id'))

    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Float, nullable=False) 
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)  # deberia ser Date
    gender = Column(String(250), nullable=False)
    
    favourites = relationship("Favourite", back_populates="people")


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    length = Column(Float(50), nullable=False)
    speed = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    cargo_capacity = Column(Integer, nullable=False)
    consumables = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)

    favourites = relationship("Favourite", back_populates="vehicle")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(Float(50), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)

    favourites = relationship("Favourite", back_populates="planet")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

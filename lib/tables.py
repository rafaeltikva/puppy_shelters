__author__ = 'rafaeltikva'

import datetime

from sqlalchemy import Column, ForeignKey, String, CHAR, Float, Integer, Date, DateTime
from sqlalchemy.orm import relationship

from database import Base

class Shelter(Base):
    __tablename__ = 'shelters'

    # create schema

    id = Column(Integer, primary_key = True)

    # Shelter name
    name = Column(String(80), nullable = False )

    # shelter address
    address = Column(String(250))

    # shelter city
    city = Column(String(250))

    # shelter state
    state = Column(String(250))

    # zip code
    zip_code = Column(Integer)

    # website url
    website = Column(String(250))

    # created date
    created_date = Column(DateTime, default = datetime.datetime.now)

    # updated date
    last_modified_date = Column(DateTime, onupdate = datetime.datetime.now)


class Puppy(Base):
    __tablename__ = 'puppies'

    # create puppy id
    id = Column(Integer, primary_key = True)

    # puppy name
    name = Column(String(80), nullable = False)

    # date of birth
    date_of_birth = Column(Date)

    # gender
    gender = Column(String(6))

    # weight
    weight = Column(Float)

    # picture url
    picture = Column(String(250))

    # shelter_id
    shelter_id = Column(Integer, ForeignKey('shelters.id'))

    # relationship with shelter
    shelter = relationship(Shelter)

    # created date
    created_date = Column(DateTime, default = datetime.datetime.now)

    # updated date
    last_modified_date = Column(DateTime, onupdate = datetime.datetime.now)





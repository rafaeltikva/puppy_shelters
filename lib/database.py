__author__ = 'rafaeltikva'

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# create base class factory
Base = declarative_base()

class Database():

    def __init__(self):

        self.engine = create_engine('sqlite:///puppies.db', echo = True)

        # initialize DB if not initialized
        self.init_db()

        # bind the engine to the base class. this makes the connection between our class definitions and the corresponding tables within our database
        Base.metadata.bind = self.engine

        # create session maker factory class
        self.Session = sessionmaker(bind = self.engine)

    def init_db(self):

        Base.metadata.create_all(self.engine)

        print("Database created")

    def get_session(self):

        return self.Session()








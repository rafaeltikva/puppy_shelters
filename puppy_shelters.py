__author__ = 'rafaeltikva'

from sqlalchemy import asc, desc
from lib.database import Database
from lib.tables import Puppy, Shelter
from lib.helpers import date_from_days_ago

def main():
    db = Database()
    session = db.get_session()

    # Exercise 1 - query all puppies in ascending order
    '''
    for row in session.query(Puppy).order_by(asc(Puppy.name)).all():
        print row.name, row.date_of_birth
    '''

    # Exercise 2 - 2. Query all of the puppies that are less than 6 months old organized by the youngest first
    '''
    for row in session.query(Puppy).filter(Puppy.date_of_birth >= date_from_days_ago(180)).order_by(desc(Puppy.date_of_birth)):
        print row.name, row.date_of_birth
    '''

    # 3. Query all puppies by ascending weight

    for row in session.query(Puppy).order_by(asc(Puppy.weight)):
        print row.name, row.weight

    # 4. Query all puppies grouped by the shelter in which they are staying

    for puppy, shelter in session.query(Puppy, Shelter).join(Shelter, Puppy.id == Shelter.id).group_by(Shelter.name):
        print puppy.name, shelter.name



main()
from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    pass

def get_all(session):
    pass

def find_by_name(session, name):
    pass

def find_by_id(session, id):
    pass

def find_by_name_and_breed(session, name, breed):
    pass

def update_breed(session, dog, breed):
    pass
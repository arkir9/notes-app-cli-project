from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Note, Category

engine = create_engine('sqlite:///notes.db')
Session = sessionmaker(bind=engine)
session = Session()

note = session.query(Note).filter_by(id=13).first()
user = session.query(User).filter_by(id=2).first()
category = session.query(Category).filter_by(id=3).first()

if user:
    note.user = user

if category:
    note.category = category

session.commit()

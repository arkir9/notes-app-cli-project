from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from notes.models import Note


engine = create_engine('sqlite:///notes.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


fake = Faker()


for i in range(10):  
    title = fake.sentence()
    content = fake.paragraph()
    note = Note(title=title, content=content)
    session.add(note)


session.commit()


session.close()

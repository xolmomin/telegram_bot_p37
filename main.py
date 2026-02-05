from sqlalchemy import insert
from sqlalchemy.orm import Session

from models import Category, User, Advert
from models.base import engine

# Base.metadata.create_all(engine)

with Session(engine) as session:
    data = [
        {
            'id': 1,
            'name': 'Texnika',
            'slug': 'texnika'
        }
    ]
    query = insert(Category).values(data)
    session.execute(query)
    session.commit()

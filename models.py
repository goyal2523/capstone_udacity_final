import os
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime

database_path = os.environ['DATABASE_URL']
if database_path.startswith("postgres://"):
  database_path = database_path.replace("postgres://", "postgresql://", 1)


db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    
    # add one demo row to each Movies and Actors

    movie = Movies(
        title='Titanic',
        release_date= datetime(2012, 3, 3)
    )


    movie.insert()

    actor = Actors(
        name='Tarun Goyal',
        age=31,
        gender='Male'
    )

    actor.insert()


# ROUTES

'''
Movies
a persistent movie entity, extends the base SQLAlchemy Model
'''


class Movies(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # String Title of the movie
    title = Column(String)
    # Release Date of the movie
    release_date = Column(Date, nullable=False)

    def view(self):
        return{
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date.strftime('%Y-%m-%d')
        }

    '''
    insert()
        inserts a new model into a database
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(Movies.view(self))

'''
Actors
a persistent actor entity, extends the base SQLAlchemy Model
'''

class Actors(db.Model):
    # Autoincrementing, unique primary key
    id = Column(Integer, primary_key=True)
    # Name of the actor
    name = Column(String)
    # Age of the actor
    age = Column(Integer)
    # gender of the actor
    gender = Column(String)

    def view(self):
        return{
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    '''
    insert()
        inserts a new model into a database
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a new model into a database
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
    '''

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(Actors.view(self))

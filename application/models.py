#import the db instance
from application import db

from sqlalchemy.dialects.mysql import YEAR

#creates the table movies into the database
class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    release = db.Column(YEAR)

#creates the table actors into the database
class Actors(db.Model):
    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date)

#creates the table cast_details into the database
#this table break the many to many relation
#between movies and actors
class Cast_details(db.Model):
    cast_it = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.movie_id'), nullable=False)
    actor_id = db.Column(db.Integer,db.ForeignKey('actors.actor_id'), nullable=False)

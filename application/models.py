#import the db instance
from application import db

from sqlalchemy.dialects.mysql import YEAR

#creates the table movies into the database
class Movies(db.Model):
    movie_it = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable = False)
    release_year = db.Column(YEAR)

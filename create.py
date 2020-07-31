# import the SQLAlchemy instance
from application import db
# import the definition of the movies table (movies class)
from application.models import Movies

#creates the table inside the db
db.create_all()

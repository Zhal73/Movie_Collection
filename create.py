# import the SQLAlchemy instance
from application import db
# import the definition of the movies table (movies class),
# actor table(Actors class) and cast_details table (Cast_datails class)
from application.models import Movies,Actors,Cast_details

#drop all existing tables, if any
db.drop_all()

#creates the table inside the db
db.create_all()

# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
# import the app object from the ./application/__init__.py
from application import app,db
#imports the db tables models
from application.models import Movies,Actors,Cast_details

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Movie Collection Home Page')

#defines route for all_movie pages
@app.route('/all_movie')
def all_movie():
    moviesData=Movies.query.all()
    return render_template('all_movie.html', title='Your Collection',posts=moviesData)

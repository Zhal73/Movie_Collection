# import render_template function from the flask module
from flask import render_template
# import the app object from the ./application/__init__.py
from application import app

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Movie Collection Home Page')

#defines route for all_movie pages
@app.route('/all_movie')
def all_movie():
 return render_template('all_movie.html', title='Your Collection')

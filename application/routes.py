# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
# import the app object from the ./application/__init__.py
from application import app,db
#imports the db tables models
from application.models import Movies
#import the form to inser a movie
from application.forms import MovieForm

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

#defines route for insert_movie pages
@app.route('/insert_movie', methods=['GET','POST'])
def insert_movie():
    form = MovieForm()
    if form.validate_on_submit():
        movieData = Movies(
                title = form.title.data,
                release = form.release.data.year
                )
        db.session.add(movieData)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('insert_movie.html', title='Insert Movie',form=form)


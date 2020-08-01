# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
# import the app object from the ./application/__init__.py
from application import app,db
#imports the db tables models
from application.models import Movies
#import the form to inser a movie
from application.forms import MovieForm, UpdateMovieForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Movie Collection Home Page')

#defines route for all_movie page
@app.route('/all_movie')
def all_movie():
    moviesData=Movies.query.all()
    return render_template('all_movie.html', title='Your Collection',posts=moviesData)

#defines route for insert_movie page
@app.route('/insert_movie', methods=['GET','POST'])
def insert_movie():
    form = MovieForm()
    if form.validate_on_submit():
        movieData = Movies(
                title = form.title.data,
                release_year = form.release_year.data
                )
        db.session.add(movieData)
        db.session.commit()

        return redirect(url_for('all_movie'))
    else:
        print(form.errors)

    return render_template('insert_movie.html', title='Add Movie',form=form)

#defines route for update page
@app.route('/update/<movie_id>', methods=['GET','POST'])
def update(movie_id):
    movie = Movies.query.filter_by(movie_id = movie_id).first()
    form = UpdateMovieForm()
    if form.validate_on_submit():
        movie.title = form.title.data,
        movie.release_year = form.release_year.data
        db.session.commit()
        return redirect(url_for('all_movie',movie_id = movie_id))
    elif request.method == 'GET':
        form.title.data = movie.title
        form.release_year.data = movie.release_year
    return render_template('update.html', title='Update Movie Details', form = form)

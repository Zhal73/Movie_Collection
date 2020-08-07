# import render_template, url_for and request functions from the flask module
from flask import render_template,redirect, url_for, request
# import the app object from the ./application/__init__.py
from application import app,db
#imports the db tables models
from application.models import Movies, Cast_details
#import the form to inser a movie
from application.forms import MovieForm, UpdateMovieForm

# define routes for / & /home, this function will be called when these are accessed
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Movie Collection Home')

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

#defines route for detele movie
@app.route('/delete/<movie_id>', methods=['GET','POST'])
def delete(movie_id):
    movie = Movies.query.filter_by(movie_id = movie_id).first()

    #this make sure that all the occurrency of movie_id in the cast details
    #are going to be deleted from Cast_details table, because it has movie_id
    #as foreign key that referes to movie_id in Movie.
    #If we don't delete the cast details, it won't be possible to delete the movie
    #because of the foreigh key costraint
    cast_details_to_delete = Cast_details.query.filter_by(movie_id = movie.movie_id).all()
    for cast_details in cast_details_to_delete:
        db.session.delete(cast_details)
        db.session.commit()

    #now is possible to delete the movie
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('all_movie'))

import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db

from application.models import Movies, Cast_details,Actors

from os import getenv



# the TestBase class contains all the necassary
# setup configuration so that the tests can be run
# and the test that will be performed
class TestBase(TestCase):
    def create_app(self):
        # pass in configurations for test database
        # this allows the test suite to connect to the database
        # using the environment variable we set when we activate the venmv
        # inside the VM
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        # this will be called every time we run a test
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        #creates a test entry for the movies table
        movie = Movies(title="Test Movie!", release_year=2000)

        #creates a test entry for the actor tables
        actor = Actors(first_name = "Jonny", last_name = "Depp",date_of_birth = '1955-01-01')

        #creates test entry for cast details
        cast = Cast_details(movie_id = 1,actor_id = 1)

        db.session.add(movie)
        db.session.add(actor)
        db.session.commit()
        db.session.add(cast)
        db.session.commit()

    def tearDown(self):
        # this will be called AFTER every test
        # this to make sure that every time we run a test
        # the database is empty and there are no duplicate
        # posts that can cause proble to the test performed.
        db.session.remove()
        db.drop_all()

##### TESTS IMPLEMENTATION  ########
class TestMovieApp(TestBase):
    pass
    # checks if the home page is accessible
    # routes.py line 14
    def test_homepage(self):
        response = self.client.get(url_for('home')) #call the home page
        self.assertEqual(response.status_code, 200) #checks if it is accessible. code : 200
    
    # checks if the all_movie page is returned
    # routes.py lines 19-20
    def test_all_movies(self):
        with self.client:
            response = self.client.get(url_for('all_movie')) #calls the all_movie page
            self.assertIn(b'Test Movie!', response.data) #checks if the name of the movie test is in the retuned page

    # checks if a new movie can be add
    # routes.py lines 25-35
    def test_insert_movie_two(self):
        with self.client:
            # calls the insert_movie page, insert the title and the release year for a new movie and follows the redirection
            response = self.client.post(url_for('insert_movie'), data=dict(title="Movie Test 2!", release_year ="1999"),follow_redirects=True )
            self.assertIn(b'Movie Test 2!',response.data)
                   
    # checks if the insert_movie page is returned
    # routes.py lines 36-38
    def test_insert_movies_one(self):
        with self.client:
            response = self.client.get(url_for('insert_movie')) #calls the all_movie page
            self.assertIn(b'Add Movie', response.data) #checks if the name of the  page is retuned

    # check if the movie details can be updates
    # route.py lines 43-49
    def test_update_two(self):
        with self.client:
            response = self.client.post(('/update/1'), data=dict(title="Movie Test 01!", release_year ="1999"),follow_redirects=True ) #update the first record in movie table
            self.assertIn(b'Movie Test 01!',response.data) #chesk if the new title is in the returned page
            self.assertNotIn(b'Test Movie!',response.data) #cheks if the old title is not in the returned page anymore

    # check if the update_movie page
    # returns the old movie detailsdetails can be updates
    # route.py lines 50-53
    def test_update_one(self):
        with self.client:
            response = self.client.get('/update/1') #calls the update_movie page
            self.assertIn(b'Test Movie!',response.data) #cheks if the old title is in the returned page

    #check if a movie can be succesful deletede
    # route.py lines 58-72
    def test_delete(self):
        with self.client:
            response = self.client.get('/delete/1') #calls the page to delete the first movie on the movies table
            self.assertNotIn(b'Test Movie!',response.data) # cheks if the old title is not in the returned page anymore

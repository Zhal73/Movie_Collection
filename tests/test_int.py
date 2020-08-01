import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Movies

# Set test variables for test movie
test_movie_title = "The Best Movie"
test_movie_release_year = 1973
test_update_title = "A movie"
test_update_release_year = 2000

#define test methods
class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/gaglianodomenico/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)


####### TEST IMPLEMENTATION ######

    # check if from the home page a user
    # is redirected to the full list of movies
    # when the correspondent link is clicked
    def test_1_home_to_all_movies(self):
        # click the link to the full list of movies
        self.driver.find_element_by_xpath('/html/body/div/a[1]').click()

        # Assert that browser redirects to all_movie page
        assert url_for('all_movie') in self.driver.current_url


    # check if from the home page a user
    # is redirected to the add_movie page
    # when the correspondent link is clicked
    def test_2_home_to_add_movies(self):
        # click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()

        # Assert that browser redirects to all_movie page
        assert url_for('insert_movie') in self.driver.current_url

    # check if from the full list of movie Page,
    # the user can return to the home page
    def test_3_all_movie_to_home(self):
        # from the home page, click the link to the full list of movies
        self.driver.find_element_by_xpath('/html/body/div/a[1]').click()
        # from the full list page, click the link to home page
        self.driver.find_element_by_xpath('/html/body/a[1]').click()

        # Assert that browser redirects to home  page
        assert url_for('home') in self.driver.current_url

    # check if from the full list of movie Page,
    # the user can navigate to the add a movie page
    def test_4_all_movie_to_add_movie(self):
        # from the home page, click the link to the full list of movies
        self.driver.find_element_by_xpath('/html/body/div/a[1]').click()
        # from the full list page, click the link add movie page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()

        # Assert that browser redirects to the inser movie page
        assert url_for('insert_movie') in self.driver.current_url
    
    # checks if a new movie can be added to the database
    def test_5_add_a_new_movie(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # fill the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_movie_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_movie_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # Assert that browser redirects to all_movie page
        assert url_for('all_movie') in self.driver.current_url

    # check if from the add movie page 
    # is possible to return to the home page
    def test_6_add_back_to_home(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # from add movie page click the link to the home  page
        self.driver.find_element_by_xpath('/html/body/a').click()
        # Assert that browser redirects to home  page
        assert url_for('home') in self.driver.current_url
    
    # check if is possible to update the
    # details of an existing movie
    def test_7_update_a_movie(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # fill the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_movie_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_movie_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # click the update link
        self.driver.find_element_by_xpath('/html/body/div/span/a[1]').click()
        # update the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_update_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_update_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # Assert that browser redirects to update page
        assert 'update' in self.driver.current_url
    
    # check if from the update page
    # is possible to go back to
    # the home page
    def test_8_update_to_home(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # fill the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_movie_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_movie_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # click the update link
        self.driver.find_element_by_xpath('/html/body/div/span/a[1]').click()
        # click the home link
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        # Assert that browser redirects to home  page
        assert url_for('home') in self.driver.current_url

    # check if from the update page
    # is possible to go to
    # the add movie page
    def test_9_update_to_add(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # fill the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_movie_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_movie_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # click the update link
        self.driver.find_element_by_xpath('/html/body/div/span/a[1]').click()
        # click the home link
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        # Assert that browser redirects to home  page
        assert url_for('insert_movie') in self.driver.current_url

    # check if from the update page
    # is possible to go to
    # the add movie page
    def test_10_delete_movie(self):
        # from home page click the link to the add movie page
        self.driver.find_element_by_xpath('/html/body/div/a[2]').click()
        # fill the form
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_movie_title)
        self.driver.find_element_by_xpath('//*[@id="release_year"]').send_keys(test_movie_release_year)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        # click the delete link
        self.driver.find_element_by_xpath('/html/body/div/span/a[2]').click()
        # Assert that browser redirects to all movie page
        assert url_for('all_movie') in self.driver.current_url




    # the tests are run
    if __name__ == '__main__':
        unittest.main(port=5000)

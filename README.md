# **<u>Movie Collection</u>** 

#### QA-SFIA Project 1

------

This is the outcome of the first personal SFIA project for the QA Academy - Week 6, as specified on:

https://portal.qa-community.co.uk/~/devops/projects/fundamental--devops



Project resources:

GitHub : https://github.com/Zhal73/Movie_Collection.git

Jira board : https://domenico-gagliano.atlassian.net/jira/software/projects/MC/boards/7/backlog



##### Index

- [Project Brief](#project-brief)
- [Requirements](#requirements)
- [General Approach](#general-approach)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Front End](#front-end)
- [Back End](#back-end)
- [CI Pipeline](#ci-pipeline)
- [Project Tracking](#project-tracking)
- [Risk Assessment](#risk-assessment)
- [Testing](#testings)
- [Future Improvements](#future-improvements)
- [Author](#author)

------

###### Project Brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

###### Requirements

The basic requirement for the application are specified on the assessment text as follow:

- Project tracking tool to cover the development of the application
- A relational database with at least 2 tables, with a relationship between them
- Produce Documentation
- Produce Risk assessment
- CRUD functionality implemented in at least one table
- Test Implementation
- Version Control
- CI server

###### General Approach

For this project I decided to develop a small application capable to manage a movie collection, on which a user will be able (once the application is fully developed) to consult a list of movie, for each movie see its cast and manage a list of actors that participate to the movies.

To implement the web application, I used the services provided by Google Cloud Platform, in particular I used a Ubuntu virtual machine to host the website and a MySQL database to host the database used by the application.

For the purpose of this assignment, the database used has a total of three tables, but I have implemented the CRUD functionality only on one table (movie table, see ERD). Further implementation are possible and I have discussed these in the [Future Improvements](#future-improvements) section.

Once I chose the topic for this project I have extended the requirements from a user perspective, I tired to define some feature that a potential user may want for an application of this kind, so I extended the requirements with the following:

- Insert new movie
- Edit a movie (edit movie's details)
- Delete a movie
- Having an Home Page
- Insert a new Actors
- Edit an Actor (edit actor's details)
- Delete an Actor
- Good-looking visual aspect
- manage a movie's cast by adding or removing actors to the cast

This brought me to skim these requirement and choose that to implement before the deadline, so that a  minimum valuable product (MVP) with the required functionality could be submitted.

To do so I have operated a MoSCoW analysis, so I could focus my effort on the functionality necessary to deliver a MVP.

My MoSCoW is specified as follow:

Must have:

- Relational Database with at least two tables with a relationship
- CRUD functionality:
  - Insert new movie
  - Edit movie
  - Delete movie
  - Retrieve the list of the movies
- Trello / Jira board
- User stories and tasks
- Full test suite
- Functioning front-end website
- Version control
- Documentation and Risk assessment



Should have:

- Home page

  

Could have:

- CRUD functionality to manage the Actors list
- CRUD functionality to manage Movie's cast



Wont have:

- Improved graphic aspects



###### Entity Relationship Diagram

To store the information related to movies, actors and cast, the database I used required three tables, a Movies table, an Actors table and a Cast_details table. The latter being necessary to manage the many-to-many relation that occurs between the Movies and the Actors table which is not possible to represent by using the relational model. 

In fact a Movie may have many actors that play different roles, and an Actor could be present in many different movies. 

The entity relationship diagram for the database is the following:



![](https://drive.google.com/uc?export=view&id=1CK7xtaftDqAEhl0NmUnhhgq0jnf9Pj0k)



In here the many-to-many relation is broken in two one to many relation, which is possible to represent in a relational model, with the use of foreign keys.

This diagram could be explained as follow:

A movie must have at least one cast details and each cast detail must be in one and only one movie.

An actors can be in many cast details (can also no be present in any) and a cast detail has one and only one actor.

###### CI Pipeline

The following is the continuous integration pipeline:

![](https://drive.google.com/uc?export=view&id=1Ror7APtmKCGE_B1UaAH_p1gYNI2AIrdb)



This highlight the tools used to test and deploy the application.

The source code has been written in Python, to  track code change I used git as version control system by using a GitHub repository available at [here](https://github.com/Zhal73/Movie_Collection.git). Using this tool allowed me to isolate the develop of new feature from the completed one, in fact every time I wanted to start the development of a new functionality, I created a different branch of the application inside the repository. Once the functionality was completed I merged the development branch, so I was sure that in the master branch I had only working software.

Every time I completed I feature, I updated the Jira board, so I was always aware of the various stage of my project.

To automate the testing and deployment of the application, I used Jenkins which is a Continuous Integration (CI) server. The CI server communicates with the Git repository by using WebHook, once change are made to the master branch, it automatically triggers the build of the testing environment and, if the test succeeds, the build of the live stage of the application.

The test environment consists in a pytest module installed into a Flask micro environment that runs in a Virtual Machine hosted by Google Cloud Platform. A similar structure is used for the live environment, where a Gunicorn production server has been implemented into the Flask microframework, which runs in the GCP virtual machine.

###### Project Tracking

To track the development cycle of this web application I used a Jira board which could is available at:

[Jira board](https://domenico-gagliano.atlassian.net/jira/software/projects/MC/boards/7/backlog)

Initially, I created a number of users stories from the project requirements requirements, then I was able to break each user story in small task that I have completed. 

![](https://drive.google.com/uc?export=view&id=1td6Lne55V41aXwdUhcS4NQAeskPIvqlC)

The previous image all the user's stories I constructed for the application. As is possible to note, each story has an associated value (story points) which indicates the estimate complexity of the story, so an higher value indicates a more complex feature to implement. As a base case for my estimation I used the story I thought was the simplest to implement, in this case the story "MC-10 Users can consult the entire movie collection", this because can be translated in a simple query.

Then I organised my job using Sprints, each of which normally last one week and included the topics studied in the previous week, so I have developed the application's functionality gradually and in line with the course evolution. The entire project was covered with a total of 4 Sprint. 

The following illustrated a typical sprint:



![](https://drive.google.com/uc?export=view&id=1hfkm833Y2rxyTXvza5Ii8b5Ta5q_1T_I)



In particular here the Sprint number four is illustrate, in here is possible to see which tasks where in the queue waiting to be addressed (TO DO), the tasks on which I was actually working (IN PROGRESS) and the tasks completed (DONE).

###### Risk Assessment

Any project is subject to risks of various nature, and this project is not an exception, so I have analysed possible risks that can affect its successful completion. I have included risks of various nature in my analysis, such as those related to the use of   Cloud Services, those related to application being available on the internet and those related to the use of the application (eg. user's input).

I also classified the Likelihood of the risks, their impact level and their tolerance by using different level, those level are defined as follow:

- **Likelihood**
  - High : the risk is likely to append because the source is technically capable, or the user is likely to make mistake in using the application.
  - Medium: the risk could happen, but controls are in place to mitigate it.
  - Low: the risk is unlikely to happened
- **Impact**
  - High : the risk occurrence can seriously lead to site malfunction or inaccessibility.
  - Medium: the risk occurrence doesn't lead to major malfunctions or loss of data.
  - Low: consequences of the risk occurrence can be recovered because effective procedure are in place
- **Risk Tolerance**
  - Tolerate: No further action taken, because the risk's consequences are manageable.
  - Treat: Action taken to minimise the risk's consequences.

| Threat                                             | Description                                                  | Likelihood | Impact | Responsibility        | Current Mitigation                                           | Proposed Mitigation                                          | Response                                                     | Tolerance |
| :------------------------------------------------- | ------------------------------------------------------------ | ---------- | ------ | --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------- |
| SQL  database Inaccessible                         | The mySql database hosted by  Google Cloud Platform cold become inaccessible, then the web application  would become unusable | Low        | Low    | Google Cloud Platform | NONE                                                         | Set up backup procedures for the  database, either by using dedicated VM or in local computer. So the DB could  be clone into another instance or moved to another provider | Try to restart the database, if  GCP is accessible otherwise contact GCP | tolerate  |
| The VM  hasting the web server become inaccessible | As the database, the webserver  for the application is running in a Virtual machine hosted by GCP. If the VM  become inaccessible, the website will not function | Low        | Low    | Google Cloud Platform | NONE                                                         | Set a backup VM so it can be run  as soon as possible,either with GCP or another provider | Try to restart the database, if  GCP is accessible otherwise contact GCP | tolerate  |
| Cross-Site  Request Forgery Attack                 | The web app make use of exchange  of information between the web server and the database, so this information  can be read and altered by using Forms. Malicious user can replicate a Form  and manipulate this while we are unaware. Even if the information store are  not sensitive, this attack can make them meaningless and unusable | Medium     | High   | Domenico Gagliano     | A environmental variable that  holds a secret key is created every time the Virtual machine is activated,  then the form use this token in a hidden field. | Implement Anti-CSRF token, using  session and cryptography for the secret key. Implement SameSite Cookies, to  disable third party usage, so requests sent from different origin are  dismisses | if the secret token is not  recognised the form gives an error | Treat     |
| Invalid  data in the forms                         | Users could accidentally insert  data that don't respect the database field requirement, such as length text,  range of date etc. | Medium     | High   | Domenico Gagliano     | WTForms validator are used when  data is submitted with a form. | Extend the use of validation.                                | If the data doesn't meet the  requirement an error is prompted to the user. | Treat     |
| HTTP  used instead of HTTPS                        | The connection to and from the  website use HTTP protocol, so data is visible by any potential attacker. | High       | Low    | Domenico Gagliano     | NONE                                                         | Implement HTTPS connection which  uses encryption to move information. | Potentially we are unaware if  malicious entity have monitored our website traffic. If we found any change  or inconsistency in the web application contents we can use backups to  restore consistency | tolerate  |
| Covid-19                                           | The infection is still around,  so it would be possible for me to catch the infection, so I won't be able to  finish the project (at least before the due date) | Low        | High   | Domenico Gagliano     | Use face cover and respect social  distance when in contact with people | Follow government directives as  they regularly change       | None                                                         | Treat     |



###### Front End

As mentioned before, the visual aspect of the application has not been developed at this stage, so the application looks very basic. It essentially consists in four html pages as described below: 

The home page is:



![](https://drive.google.com/uc?export=view&id=1WGT6M67cNB5ZU_jcPlfwKE8homG-2n_M)

It consists in a welcome message, a link to a page that read the entire content of the movie table, and a link to a page tat allows the user to add an new movie to the collection.

The page that shows the movie list is:



![](https://drive.google.com/uc?export=view&id=14-GUqpsugDdjwX1W4TpBKyHDrQfUPx64)



In here the user, other than see the entire list of movies, is presented with two further links for each movie to update the details of the movie or to delete it from the list.

The page to add a movie to the list is:



![](https://drive.google.com/uc?export=view&id=1KObfG7KbTAYbcUcyi6VRAfZW_CuPRBaz)

In here the user is able to put the details of the new movie to be added.

The data insert in each field is validate before it is submitted, in particular the movie title has to be between 2 and 100 characters long, and the release year has to be from 1900 to the current year, so it is not possible to add "future" movie.



![](https://drive.google.com/uc?export=view&id=1rUDSnpM2s6vh0iRt3tPYgWBgPjiI4plX)

The piece of code that checks the year validity is:

*release*_year = IntegerField('Release Year : ',*
            *validators = [*
                *NumberRange(*
                    *min=1900,*
                    *max=date.today().year)*
            *]*
        )*

The same structure is reproduced for the page that update movies details:



![](https://drive.google.com/uc?export=view&id=1XXwfGiTucUC_fSVy2cfhznsNZMNAO_RM)

when the user clicks the link, the page retrieve the movie details from the database, and automatically fills the field in the form, so the user is able to see what information is stored on the database. Again validation is in place to make sure that the user insert appropriate details.

###### Back End

the back end implementation uses the micro framework Flask, this allowed me to program the application in Python. As a micro framework, Flask can be extended with the use of modules that implement particular functionality I may need.

The whole implementation was hosted in a GCP virtual machine, but Flask has been installed into a virtual environment crated with  python3-venv, this to avoid possible software conflicts with the VM.

Inside the virtual environment I installed the necessary modules, in particular I used:

- SQLAlchemy to be able to write queries for the database, using python
- pymysql to manage the connection with the database
- WTForm to manage write forms in python and perform validation

The application's structure is a typical Flask structure:



![](https://drive.google.com/uc?export=view&id=1FkvJcLbaYn2eXCUwrW2trjmkkXcWL9vw)





Here I  have the apllication nested into the application directory, inside of which is possible to find the python files to manage forms (forms.py), database models (models.py) and routes (routes.py). Inside the application directory I have the template directory which contains the html pages. These pages are called inside the routes.py functions defined with @app.route, this functions uses the render_template library to return the appropriate html page.

###### Testing

The application tests have been done by using the Python modules pytest.

--- Unit Testing ---

Before the implementation of any test, I had a situation similar to this:



![](https://drive.google.com/uc?export=view&id=1Ru2oQekRWCH6PKOmmukiLQBsLaa8ZJao)



so I needed to implement unit tests to increase the coverage of the feel routes.py. 

My approach for this was to return to the lines of code highlighted on the report and start to write test function for the specific lines. For example the following checks if the home pages is called correctly by the route definition inside route.py

`# checks if the home page is accessible `
`# routes.py line 14    `

`def test_homepage(self):        `

`response = self.client.get(url_for('home')) `

`#call the home page        `

`self.assertEqual(response.status_code, 200) #checks if it is accessible. code : 200`

I repeated the process for all the other lines specified on the report, I wrote a total of eight tests to reach a coverage of 100%. 

The following image shows the a part of the Jenkins console output after the test have been performed:



![](https://drive.google.com/uc?export=view&id=1fhGZF8ibreA1RnbsainrEtgLI9H3SG9D)



--- Integration Testing ---

I  used a similar approach for the integration testing. For this purpose I used Selenium and Chomedriver.

I tried to check all the possible integration between the various part of the application, in particular I wrote test make sure that the links were able to redirect to the intended page, I checked that was possible to fill the forms to add and update movie and if it wad possible to delete movie.

I wrote a total of ten test which didn't return any error.

The following is a an example of the tests I wrote, in particular this test checks if is possible to update a movie's details:

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

Here is possible to see that the webdriver performs the following actions: 

1.  From the home page it clicks the link to the add a movie page 
2.  It fills the form
3. it submit the form
4. then the test checks if it is redirected to the full list of movies.

###### Future Improvements

The application is indeed in a very initial state, so further improvement could consist in adding functionality to manage the list of Actors, manage the Cast for each movie and perform some search functionality such as search for a specific movie tile, or actor, other than improve the graphical aspect of the application.



###### Author

Domenico Gagliano
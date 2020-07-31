#importe the module FlaskForm to implement Forms
from flask_wtf import FlaskForm
#import the necessary data type to use in the field
from wtforms import StringField, IntegerField, DateField,SubmitField
#import the necessary validator to make sure that
#the data inserted is of the valid format
from wtforms.validators import DataRequired, Length
#import the Movies class defined in model.py
from application.models import Movies

#creates the Form to insert a new movie:
class MovieForm(FlaskForm):
    title = StringField('Movie Title : ',
            validators = [
                DataRequired(),
                Length(min=2, max=100)
            ]
        )
    """
    release = StringField('Release Year : ',
            validators = [
                Length(min=4, max=4)
                ]
        )
    """
    release = DateField('Release Year : ',format='%Y',
        )
    submit = SubmitField('Add Movie')


#importe the module FlaskForm to implement Forms
from flask_wtf import FlaskForm
#import the necessary data type to use in the field
from wtforms import StringField, IntegerField, DateField,SubmitField
from wtforms.validators import NumberRange
from wtforms_components import DateRange
from datetime import date
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
    """
    release_year = DateField('Release Year : ',
            validators = [
                DateRange(
                max=date.today().year)
            ]
        )
    submit = SubmitField('Add Movie')
    """
    release_year = IntegerField('Release Year : ',
            validators = [
                NumberRange(
                    min=1900,
                    max=date.today().year)
            ]
        )
    submit = SubmitField('Add Movie')

from flask_wtf import Form
from wtforms import StringField, SelectMultipleField
from wtforms.validators import InputRequired, Length, ValidationError
import datetime

def isValidInteger(form, field):
    try:
        int(field.data)
    except ValueError:
        raise ValidationError('Field must be of valid zipcode format')


def validateDateFormat(form, field):
    try:
        datetime.datetime.strptime(field.data, '%Y-%m-%d')

    except ValueError:
        raise ValidationError('Date must be in yyyy-mm-dd format')


def datesArePossible(form, field, startDate):
    if field.data.date.replace('/', '') < startDate.replace('/', ''):
        raise ValidationError('End date can\'t be predate the start date')


class SearchForm(Form):
    zipcode = StringField('zipcode', validators=[InputRequired(), Length(min=5, max=7), isValidInteger])

    startDate = StringField('startDate', validators=[InputRequired(), validateDateFormat])
    endDate = StringField('endDate', validators=[InputRequired(), validateDateFormat])

    categories = SelectMultipleField('categories')
    

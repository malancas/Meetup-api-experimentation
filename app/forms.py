from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length, ValidationError
import re

def isValidInteger(form, field):
    try:
        int(field.data)
    except ValueError:
        raise ValidationError('Field must be of valid zipcode format')

def validateDateFormat(form, field):
    dateRegEx = '/^(0[1-9]|1[012]|[1-9])[- /.](0[1-9]|[12][0-9]|3[01]|[1-9])[- /.](19|20)\d\d$/'

    if not re.match(dateRegEx, field.data):
        raise ValidationError('Date must be in mm/dd/yyyy format')

class SearchForm(Form):
    zipcode = StringField('zipcode', validators=[DataRequired(), Length(min=5, max=7), isValidInteger])
    startDate = StringField('startDate', validators=[DataRequired()])
    endDate = StringField('endDate', validators=[DataRequired()])

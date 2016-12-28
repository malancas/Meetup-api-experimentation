#!opt/anaconda/bin/flask
import os
import unittest
from app import forms
from wtforms.validators import InputRequired, Length, ValidationError


class AppTestCase(unittest.TestCase):
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
    

    def test_isValidInteger():
        assert(forms.isValidInteger(2.0) == 2)
        self.assertRaises(Validation, forms.isValidInteger(2.5))

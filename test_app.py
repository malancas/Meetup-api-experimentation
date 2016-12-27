#!opt/anaconda/bin/flask
import os
import unittest
from app import forms

def test_isValidInteger():
    assert(forms.isValidInteger(2.0) == 2)
    assert(forms.isValidInter(2.5) != 2)
    unittest.assertRaises(Validation, isValidInteger(2.5))

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertRaises(ValidaitonError, isValidInteger(2.5))

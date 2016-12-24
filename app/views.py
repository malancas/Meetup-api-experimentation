from flask import render_template, redirect, flash, request
from app import app
from .forms import SearchForm
import requests

'''
Ask for zipcode of vacation.
Ask for dates one will be on vacation.
Use categories of subscribed groups
to find similar groups in the given area code
'''

@app.route('/')
@app.route('/index')
def index():
    cats = requests.get("https://api.meetup.com/2/categories?key=50435526d4215731a6973f07d5d50&sign=true")
    user = {'nickname': 'Meredith'}
    return render_template('index.html',
                           title='Home',
                           user=user, cats=cats.json())

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if form.validate_on_submit():
        return results(form)
    return render_template('search.html', 
                           title='Search',
                           form=form)

def results(form):
    #groups = requests.get("https://api.meetup.com/find/groups?key=50435526d4215731a6973f07d5d50&sign=true")
    
    groups = requests.get("https://api.meetup.com/find/groups?key=50435526d4215731a6973f07d5d50&sign=true&photo-host=public&zip=10514&page=20")
    return render_template('results.html',
                           title='Meetup results',
                           groups=groups.json())

    

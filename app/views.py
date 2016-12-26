from flask import render_template, redirect, flash, request
from app import app
from .forms import SearchForm
from datetime import datetime
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
    # Use the Google Maps API to grab information about the city corresponding to the zipcode given.
    payload = {'address': form.zipcode.data}
    cityData = requests.get("https://maps.googleapis.com/maps/api/geocode/json", payload).json()

    lat = str(cityData['results'][0]['geometry']['location']['lat'])
    lng = str(cityData['results'][0]['geometry']['location']['lng'])
    
    # Can use latitude and longitude data in the cityData result to search for local events
    payload = {'lat': lat, 'lon': lng, 'key': '50435526d4215731a6973f07d5d50', 'sign': 'true'}
    events = requests.get("https://api.meetup.com/find/events", payload).json()

    # Convert given dates to UTC time to find events
    startDate = form.startDate.data.split('-',3)
    startDate = [int(num) for num in startDate]
    endDate = form.endDate.data.split('-',3)
    endDate = [int(num) for num in endDate]

    utcStart = datetime(startDate[0], startDate[1], startDate[2]).timestamp() * 1000
    utcEnd = datetime(endDate[0], endDate[1], endDate[2]).timestamp() * 1000
    availableEvents = []
    for event in events:
        if utcStart <= float(event['time']) <= utcEnd:
            availableEvents.append(event)

    return render_template('results.html',
                           title='Meetup results',
                           events=availableEvents)

    

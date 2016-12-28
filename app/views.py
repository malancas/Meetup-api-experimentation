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

@app.route('/search', methods=['GET', 'POST'])
def search():
    payload = {'key': '50435526d4215731a6973f07d5d50', 'sign': 'true'}
    jsonCategories = requests.get("https://api.meetup.com/2/categories", payload).json()
    jsonCategories = jsonCategories["results"]

    categoryDict = {}
    categories = []
    for jsonCategory in jsonCategories:
        categoryDict[jsonCategory["name"]] = str(jsonCategory["id"])
        categories.append(jsonCategory["name"])

    form = SearchForm(request.form)
    form.categories.choices = categories


    if form.validate_on_submit():
        return results(form, categoryDict)
    return render_template('search.html', 
                           title='Search',
                           form=form, categories=categories)

def results(form, categoryDict):
    # Use the Google Maps API to grab information about the city corresponding to the zipcode given.
    payload = {'address': form.zipcode.data}
    cityData = requests.get("https://maps.googleapis.com/maps/api/geocode/json", payload).json()

    lat = str(cityData['results'][0]['geometry']['location']['lat'])
    lng = str(cityData['results'][0]['geometry']['location']['lng'])
    
    categories = request.form.getlist('selectcategories')

    # Can use latitude and longitude data in the cityData result to search for local events
    chosenCategories = ''
    for category in categories:
        chosenCategories += (categoryDict[category] + ',')
    chosenCategories = chosenCategories[:-1]

    # Convert given dates to UTC time to find events
    startDate = form.startDate.data.split('-',3)
    startDate = [int(num) for num in startDate]
    endDate = form.endDate.data.split('-',3)
    endDate = [int(num) for num in endDate]

    utcStart = datetime(startDate[0], startDate[1], startDate[2]).timestamp() * 1000
    utcEnd = datetime(endDate[0], endDate[1], endDate[2]).timestamp() * 1000

    timeRange = str(int(utcStart)) + ',' + str(int(utcEnd))


    payload = {'zip': form.zipcode.data, 'category': chosenCategories, 'time': timeRange,  'key': '50435526d4215731a6973f07d5d50', 'sign': 'true'}
    open_events = requests.get("https://api.meetup.com/2/open_events", payload).json()

    if open_events:
        open_events = open_events["results"]

    availableEvents = []
    for event in open_events:
        if utcStart <= float(event['time']) <= utcEnd:
            availableEvents.append(event)

    return render_template('results.html',
                           title='Meetup results',
                           events=availableEvents)

    

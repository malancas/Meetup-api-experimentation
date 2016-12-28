from flask import render_template, redirect, flash, request
from app import app
from .forms import SearchForm
from datetime import datetime
import requests

@app.route('/')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # Get all event categories in json object format and store them in a list
    payload = {'key': '50435526d4215731a6973f07d5d50', 'sign': 'true'}
    jsonCategories = requests.get("https://api.meetup.com/2/categories", payload).json()
    jsonCategories = jsonCategories["results"]

    # Parse the json objects and store the corresponding category names and ids in a dictionary. Also store the names in a list
    categoryDict = {}
    categories = []
    for jsonCategory in jsonCategories:
        categoryDict[jsonCategory["name"]] = str(jsonCategory["id"])
        categories.append(jsonCategory["name"])

    # Make the search form and set the list of category names
    # as options in the multiple selection field on the search page
    form = SearchForm(request.form)
    form.categories.choices = categories

    # If the form validates, show the user the results page
    # Otherwise, return them to the search page
    if form.validate_on_submit():
        return results(form, categoryDict)
    return render_template('search.html', 
                           title='Search',
                           form=form, categories=categories)


def results(form, categoryDict):
    # Get the selected categories
    categories = request.form.getlist('selectcategories')

    # Store the chosen categories' id in a string that will be
    # used in an api call
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

    # Place the start date and end date in UTC format in a string
    # to be used in the payload of the open_events api call
    timeRange = str(int(utcStart)) + ',' + str(int(utcEnd))

    payload = {'zip': form.zipcode.data, 'category': chosenCategories, 'time': timeRange,  'key': '50435526d4215731a6973f07d5d50', 'sign': 'true'}
    open_events = requests.get("https://api.meetup.com/2/open_events", payload).json()

    # If the result isn't empty, reset open_events to the list
    # of event dictionary objects stored in open_events["results"]
    if open_events and "results" in open_events:
        open_events = open_events["results"]
    else:
        open_events = []

    return render_template('results.html',
                           title='Meetup results',
                           events=open_events)

    

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

import time
import datetime
def convertUtcToDate(utcTime, utcOffset):
    return time.strftime('%m-%d-%Y %I:%M %p', time.gmtime((utcTime+utcOffset) / 1000.0))

app.jinja_env.globals.update(convertUtcToDate=convertUtcToDate)

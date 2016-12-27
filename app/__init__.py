from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

import time
def convertUtcToDate(utcTime):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(utcTime))

app.jinja_env.globals.update(convertUtcToDate=convertUtcToDate)

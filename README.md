# Experimenting with the Meetup API - Meetup on Vacation, Business, etc.

### This is a small web app that uses the Meetup API to explore how it can be used to help meetup users find events when they are visiting cities on business trips or vacation. The idea behind it was to encourage those who may be visiting to check out the local communities of their choosing. It could also be used by those considering moving to a new area to scout out communities they may be interested in. I also considered how it could be used to encourage cross country or international networking. While this is implemented as a web app, it seems like a feature that could be added to the mobile app or website.

### Dependencies: 
- [python>=3.5.2](https://www.python.org/downloads/release/python-352/)
- [flask](http://flask.pocoo.org/)
- [flask-wtf](https://flask-wtf.readthedocs.io/en/stable/)

### To run the application locally

### 1. Clone this repository.

```Bash
yourmachine:~$ git clone https://github.com/malancas/Meetup-api-experimentation.git
```

### 2. Change the python path at the top of ***run.py*** to the appropriate path on your machine

### 3. Execute the ***run.py*** file.

```Bash
yourmachine:~$ python run.py
```

### 4. Direct your browser to http://localhost:5000/search. 
- Enter the zipcode of your location
- Enter your start and end dates for availability in the format ***yyyy-mm-dd***
- Select event categories that interest you
- Click on **Find meetups!** to view relevant Meetups
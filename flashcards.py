from datetime import datetime

from flask import Flask, render_template

from model import db

app = Flask(__name__)


@app.route('/')
def home():
    data = ({"name": "Sunil", "lastname": "Kumar", "age": 24 })
    return render_template('welcome.html', data=data)


@app.route('/card')
def card():
    data = db[0]
    return render_template('card.html', data=data)


@app.route('/date')
def date():
    return "This page was server at " + str(datetime.now())


counter = 0


@app.route('/count_views')
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + "times"
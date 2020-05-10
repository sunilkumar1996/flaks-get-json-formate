from datetime import datetime

from flask import Flask, render_template, jsonify, redirect, request, url_for

from model import db

app = Flask(__name__)


@app.route('/')
def home():
    data = ({"name": "Sunil", "lastname": "Kumar", "age": 24 })
    return render_template('welcome.html', data=data)


@app.route('/card')
def card():
    data = db
    return jsonify({"data": data})
    # return render_template("card.html", data=data)


@app.route('/date')
def date():
    return "This page was server at " + str(datetime.now())


counter = 0


@app.route('/count_views')
def count_views():
    global counter
    counter += 1
    return "This page was served " + str(counter) + "times"


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid username and password."
        else:
            return redirect(url_for('card'))
    return render_template('login.html', error=error)


app.run(debug=True)
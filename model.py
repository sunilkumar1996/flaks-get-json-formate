"""
model.py
--------
Implement the model for our website by simulating a database.
https://flask-sqlalchemy.palletsproject.com/
"""
import json


def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)


db = load_db()
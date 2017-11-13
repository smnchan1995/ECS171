import os

from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
from flask_sqlalchemy import SQLAlchemy

import dbaccess
 
app = Flask(__name__)
app.config.from_pyfile("settings.cfg")

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://%s:%s@%s:%s/%s" % (app.config['DB_USER'],
	app.config['DB_PASS'], app.config['DB_HOST'], app.config['DB_PORT'], app.config['DB_NAME'])


db = SQLAlchemy(app)

Joke = dbaccess.buildJokeModel(db)
JokeRater = dbaccess.buildJokeRaterModel(db)
JokeRating = dbaccess.buildJokeRatingModel(db)
 
@app.route("/")
def index():
    return render_template(
    'index.html',**locals())
 
@app.route("/starwars/<string:location>/")
def colors(location):
    if location == "low":
        colorName = "red"
        other = "high"
        imageSource = "http://www.thegeekedgods.com/wp-content/uploads/2017/05/SW-Debate-04.jpg"
    elif location == "high":
        colorName = "blue"
        other = "low"
        imageSource = "http://i.imgur.com/nMoSrfz.jpg"
    return render_template(
    'main.html',**locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

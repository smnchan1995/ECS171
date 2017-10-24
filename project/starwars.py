from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint
 
app = Flask(__name__)
 
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
    'test.html',**locals())
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
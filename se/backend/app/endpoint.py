import requests
from flask import Flask, flash, redirect, render_template, request, session, abort
import jokes 

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def usernameRules():
    user = request.get_json()
    return user['username'] + " Rules!\n"

@app.route('/test', methods = ['GET'])
def test():
	return "Hello, I'm the endpoint!"

@app.route('/joke_test', methods=['GET'])
def root():
    return app.send_static_file('joke_test.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    return jokes.getRandomJoke()

if __name__ == "__main__":
    app.run(host='localhost')

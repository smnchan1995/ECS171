import requests
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def usernameRules():
    user = request.get_json()
    return user['username'] + " Rules!\n"

@app.route('/test', methods = ['GET'])
def test():
	return "Hello, I'm the endpoint!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
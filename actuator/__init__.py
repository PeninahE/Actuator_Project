# __init__.py
#from requests import requests
import requests
from flask import Flask, render_template, redirect, request


def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route('/hello')
    def hello ():
        return "hello world"

    @app.route('/')
    def app_html():
        #status_choice = "health"
        return render_template("app_html.html")
        #return render_template("health.html", result="health data", status_choice=status_choice)
    @app.route('/actuator', methods=['POST', 'GET'])
    def actuator():
        if request.method == 'POST':
            status_choice = request.form['status']
        elif request.method == 'GET':
            status_choice = request.args.get('status')

        url = "http://127.0.0.1:8000/pyctuator/" + status_choice
        actuator_response = requests.get(url)

        status_choice = "health"
        return render_template("base_template.html", result = "health data", status_choice = status_choice)

    return app


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
        return render_template("app_html.html")

    @app.route('/actuator', methods=['POST', 'GET'])
    def actuator():
        status_choice = request.form['status']
        url = "http://127.0.0.1:8000/pyctuator/" + status_choice
        actuator_response = requests.get(url)

        if status_choice == "health":
            return render_template("health.html", result = "health data", status_choice = status_choice)

        elif status_choice == "metrics":
            #return redirect("http://127.0.0.1:8000/pyctuator/metrics")
            return render_template("metrics.html", result=actuator_response.text)

        elif status_choice == "env":
            return render_template("env.html", result=actuator_response.text)

        elif status_choice == "logfile":
            return render_template("logfile.html", result = actuator_response.text)

        elif status_choice == "httptrace":
            return render_template("httptrace.html", result = actuator_response.text)

        elif status_choice == "threaddump":
            return render_template("threaddump.html", result = actuator_response.text)

    return app


 #
 # <!-- {% block status %}
 #        { % if {{status_choice}} == "health" %}
 #         { % include "health.html" %}
 #
 #        { % elif status == "metrics" %}
 #         { % include "metrics.html" %}
 #
 #        { % elif status == "env" %}
 #         { % include "env.html" %}
 #
 #        { % elif status == "logfile" %}
 #         { % include  "logfile.html" %}
 #
 #        { % elif status == "httptrace" %}
 #         { % include "httptrace.html" %}
 #
 #        { % elif status == "threaddump" %}
 #         { % include "threaddump.html" %}
 #        {% endif %}
 #     {% endblock %} -->
#
# < !--{ % extends
# "base_template.html" %}
# { % block
# title %}Server
# Health
# Status
# { % endblock %}
#
# { % block
# status_choice %}
# {{result}}
# { % endblock %}
#
# -->

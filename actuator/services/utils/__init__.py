
#__init__.py
from flask import Flask, render_template
from actuator.services import ServiceCaller

def create_app():
    # create and configure the app
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Hello, World. Welcome to my class project!'
    @app.route('/service')
    def service():
        json_response = ServiceCaller("http://service.call.url.com")
        return render_template('results.html', json_response = json_response)


        @app.route("/pyctuator/<page>")
        def im_research(page):
            result = get_actuator_results()
            return render_template("result.html", page=page, result=result)
        #
        # { % if endpoint == "Health" %}
        # { % include  "health.html" %}
        #
        # { % elif endpoint == "metrics" %}
        # { % include "metrics.html" %}


    return app
#conftest.py
import pickle

import pytest
from flask import template_rendered

from actuator import create_app


#from c21_project_web_app_structure.site_visualization import create_app, SiteLoader

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

# @pytest.fixture
# def captured_templates(app):
#     recorded = []
#
#     def record(sender, template, context, **extra):
#         recorded.append((template, context))
#
#     template_rendered.connect(record, app)
#     try:
#         yield recorded
#     finally:
#         template_rendered.disconnect(record, app)
#
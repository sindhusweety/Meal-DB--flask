#!/usr/bin/env python3.9

from flask import Flask
from flask_cors import CORS # enable it for all use cases on a domain


def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__)
    CORS(app)

    from . import meal_app
    app.register_blueprint(meal_app.meal_app)


    return app
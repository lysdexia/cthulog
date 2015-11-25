# -*- coding: utf-8 -*-
import os
"""
flask automagically includes ALL_CAPS values in the app.config object
(see main.py app.config.from_object)
"""
# path to use when daemonized
basedir = os.path.abspath(os.path.dirname(__file__))

# Yeah, this is overkill
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# authentication is in it's own file.
APP_SECRET_KEY = "changemefoolseriously"

EDITORS = {"email@example.com": "doublesecret"}

del os

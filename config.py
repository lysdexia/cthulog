# -*- coding: utf-8 -*-
import os
"""
flask automagically includes ALL_CAPS values in the app.config object
(see main.py app.config.from_object)
"""
# path to use when daemonized
basedir = os.path.abspath(os.path.dirname(__file__))

# authentication is in it's own file.
APP_SECRET_KEY = "changemefoolseriously"

MONGOLAB_URI = os.environ["MONGOLAB_URI"]

EDITORS = {"email@example.com": "doublesecret"}

del os

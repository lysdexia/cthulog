# -*- coding: utf-8 -*-
import os
"""
flask automagically includes ALL_CAPS values in the app.config object
(see main.py app.config.from_object)
"""
# path to use when daemonized
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = os.path.join(basedir, "cthulog.db")
SCHEMA = os.path.join(basedir, "cthulog-schema.sql")

# authentication is in it's own file.
APP_SECRET_KEY = "changemefool"

EDITORS = {"email@example.com": "doublesecret"}

del os

# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
"""
flask automagically includes ALL_CAPS values in the app.config object
(see main.py app.config.from_object)
"""
# path to use when daemonized
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, ".env"))

APP_SECRET_KEY = os.environ["APP_SECRET_KEY"]
MONGOLAB_URI = os.environ["MONGOLAB_URI"]
ADMINS = {"email@example.com": "doublesecret"}
PLACENAME = "Cthulog"

DEBUG = True
TEMPLATE_DEBUG = False

del os

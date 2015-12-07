import re
from flask import request
from flask.ext import restful
from flask_restful import reqparse

"""
TODO set up databases
messages
users
hates
"""

def opression_api(app, mongo):

    class Read(restful.Resource):
        """
        read must have token from supplicant
        """
        def post(self):
            doc = request.get_json()
            posts = mongo.db.posts.find(doc["args"]).sort([("stamp", -1)]).limit(100)
            return {
                    "section": doc["section"],
                    "posts": "convert posts to json before you send them"
                    }

    class Write(restful.Resource):
        """
        write must have token from supplicant
        """
    class Read(restful.Resource):
        def post(self):
            doc = request.get_json()
            posts = mongo.db.posts.find(doc["args"]).sort([("stamp", -1)]).limit(100)
            return {
                    "section": doc["section"],
                    "posts": "convert posts to json before you send them"
                    }

        def post(self):
            return "I know NUTZINK!"

    class Supplicant(restful.Resource):
        def post(self):
            doc = request.get_json()
            message_id = doc["message_id"]
            # test only grabbed from db with userid
            difficulty = 4
            return {
                    "difficulty": "0" * difficulty,
                    "message_id": message_id,
                    }

    api = restful.Api(app)
    api.add_resource(Read, "/read")
    api.add_resource(Write, "/write")
    api.add_resource(Supplicant, "/oppression/supplicant")

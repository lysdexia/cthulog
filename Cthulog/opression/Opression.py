import re
from flask import request
from flask.ext import restful
from flask_restful import reqparse

def opression_api(app):

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
    api.add_resource(Supplicant, "/oppression/supplicant")

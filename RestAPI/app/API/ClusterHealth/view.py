try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APIspec
    from marshmallow import Schema, fiields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    print("import okeh")
except Exception as e:
    print("Error:{}".format(e))

class HealthController(Resource):
    
    @doc(description =  'ini healty endpoint', tags=['Health Endpoint'])

    def get(self):
        return{'message': 'API bekerja'},200

    
from apispec import APISpec


try:
    from flask import Flask
    from flask_restful import Resource, Api
    from apispec import APIspec
    from marshmallow import Schema, fiields
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from flask_apispec.views import MethodResource
    from flask_apispec import marshal_with, doc, use_kwargs

    from API.ClusterHealth.view import HealthController
except Exception as e:
    print("__init Modules Tidak Ditemukan{}".format(e))

app = Flask(__name__)
api = API(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
    title = 'Awesome Project',
    version='v1'
    plugins=[MarshmallowPlugin()]
    openapi_version='2.0.0'),
    'APISPEC_SWAGGER_URL': '/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/swaggerui/'
})
docs = FlaskApiSpec(app)
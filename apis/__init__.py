from flask_restplus import Api

from .namespace1 import api as ns1

api = Api(
    title='Py-Mapper',
    version='0.1',
    description='Process to take a list of JSON objects and convert them into a different list of JSON Objects with different keys based off of a Mapping Key'
    # All API metadatas
)

api.add_namespace(ns1)
from flask import request
from flask_restplus import Namespace, Resource, fields

from service.mapper.BasicMap import BasicMap as BM

INPUT_DATA_EXAMPLE = [{'Fname':'Cody','Lname':'Zimmerman'}, {'Fname':'Jeremy','Lname':'Leininger'}]
MAP_KEY_EXAMPLE = [{"Fname":"FirstName"}, {"Lname":"LastName"}]

api = Namespace('basic-map', description='Maps one JSON Object to another JSON Object based off of a map key')

basic_input = api.model('Basic Input', {
    'input_data': fields.List(fields.Wildcard(fields.String), example=INPUT_DATA_EXAMPLE),
    'map_key': fields.List(fields.Wildcard(fields.String), example=MAP_KEY_EXAMPLE)
})

@api.route('/')
class BasicMap(Resource):
    @api.expect(basic_input)
    @api.doc('basic_map')
    def post(self):
        #print(request.json)
        input_list = request.json['input_data']
        map_key = request.json['map_key']

        print(input_list)
        print(map_key)
        return BM.MapList(input_list, map_key)
        
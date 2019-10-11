import json
from jsonschema import validate
from service.schema.BasicMapKeySchema import BasicMapKeySchema
class BasicMap():

    @staticmethod
    def Map(input_object, map_key):
        _map_key = BasicMap._validatemapkey(map_key)
        BasicMap._mapdata(input_object, _map_key)


    @staticmethod
    def _validatemapkey(map_key):
        _map_key = None
        try:
            _map_key = json.loads(map_key)
        except json.decoder.JSONDecodeError as e:
            print(f'Error processing Map Key: {map_key}')
            print(str(e))
            raise Exception()

        schema = BasicMapKeySchema().MapKeySchema()
        try:
            validate(_map_key, schema)
        except Exception as e:
            print(str(e))

        return _map_key

    @staticmethod
    def _mapdata(input_object, map_key):

        mapped_data = {}
        for key in input_object & map_key:
            print(key)

        
import json
from jsonschema import validate
from service.schema.BasicMapKeySchema import BasicMapKeySchema
class BasicMap():

    @staticmethod
    def Map(input_object, map_key):
        _map_key = BasicMap._validatemapkey(map_key)
        return BasicMap._mapdata(input_object, _map_key)

    @staticmethod
    def MapList(input_list, map_key):
        _map_key = BasicMap._validatemapkey(map_key)
        return BasicMap._maplistdata(input_list, _map_key)


    @staticmethod
    def _validatemapkey(map_key):
        _map_key = None

        try:
            json.dumps(map_key)
        except (TypeError, OverflowError):
            print('Failure! :(')
        else:
            return map_key

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
        for ind_dict in map_key:
            for k,v in ind_dict.items():
                if k in input_object.keys():
                    mapped_data[v] = input_object[k]

        if mapped_data == {}:
            raise Exception("No values mapped.")
        return mapped_data


    @staticmethod
    def _maplistdata(input_list, map_key):

        mapped_data = []

        for item in input_list:
            new_item = {}
            for k, v in item.items():
                print(f'k :{k}')
                print(f'v :{v}')
                for ind_map in map_key:
                    for km, vm in ind_map.items():
                        if km == k:
                            print(f'km {km}')
                            print(f'vm {vm}')
                            new_item[vm] = v
            
            mapped_data.append(new_item)
                            
        return mapped_data  
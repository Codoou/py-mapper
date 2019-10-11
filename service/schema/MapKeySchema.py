from jsonschema import validate

class MapKeySchema():

    def __init__(self):


        #[
        #    {
        #      "map": {
        #          "Lname":"LastName"
        #      },
        #      "type": "str",
        #      "nullable": [True, False],
        #      "type_validation": ['Raise', 'SilentlyContinue', 'MapWithoutTypeChange'] 1. Stop | 2. Don't Map, Don't Error | 3. Map with incorrect type
        #    },
        #    {
        #      "map": {
        #          "Fname":"FirstNameName"
        #      },
        #      "type": "str",
        #      "nullable": [True, False],
        #      "type_validation": ['Raise', 'SilentlyContinue', 'MapWithoutTypeChange']
        #    },
        # ]
        self.schema = {
            "type": "object",
            


        }

    def MapKeySchema(self):
        return self.schema
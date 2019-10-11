class BasicMapKeySchema():

    def __init__(self):
        self.schema = {
            "type": "array",
            "items": {
                "type":"object"
            }
        }

    def MapKeySchema(self):
        return self.schema
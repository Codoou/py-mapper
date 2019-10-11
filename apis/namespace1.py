from flask_restplus import Namespace, Resource, fields

api = Namespace('Basic Map', description='Maps one JSON Object to another JSON Object based off of a map key')

cat = api.model('Cat', {
    'id': fields.String(required=True, description='The cat identifier'),
    'name': fields.String(required=True, description='The cat name'),
})

CATS = [
    {'id': 'felix', 'name': 'Felix'},
]

@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS
from collections import OrderedDict

from flask import Flask
from flask_restplus import fields, Api, Resource

app = Flask(__name__)
api = Api(app)

my_model = api.model('GoodsModel', {
    'task': fields.String,
    'uri': fields.Url('todo_ep')
})


class MyDao(object):

    def __init__(self, id, task):
        self.id = id
        self.task = task

        self.status = 'active'

@api.route('/togo')
class Togo(Resource):

    @api.marshal_with(my_model)
    def get(self, **kwargs):
        return MyDao(id='my_todo', task='Remember the milk')


if __name__ == '__main__':
    app.run(debug=True)

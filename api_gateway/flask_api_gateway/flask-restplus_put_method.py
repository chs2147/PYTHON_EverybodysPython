from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

inventory = {}


@api.route('/inventory/<string:inventory_id>')
class InventoryManagement(Resource):

    def get(self, inventory_id):

        if inventory_id not in inventory.keys():
            return {"N/A": "N/A"}

        return {inventory_id: inventory[inventory_id]}

    def put(self, inventory_id):
        inventory[inventory_id] = request.form['data']
        return {inventory_id: inventory[inventory_id]}


if __name__ == '__main__':
    app.run(debug=True)

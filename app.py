from flask import Flask
from flask_restful import Resource, Api
from Category import Category, CategoryName, CategoryId


class Online(Resource):
    def get(self):
        return {'status': 'online'}


app = Flask(__name__)
api = Api(app)

api.add_resource(Online, '/')
api.add_resource(Category, '/category')
api.add_resource(CategoryName, '/category/name/<category_name>')
api.add_resource(CategoryId, '/category/<category_id>')


if __name__ == '__main__':
    app.run(debug=True)

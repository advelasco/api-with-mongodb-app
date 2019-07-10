import datetime
import uuid
from flask import Flask, jsonify
from pymongo import MongoClient
from flask_restful import Resource, Api, reqparse


class CategoryRepository:
    def __init__(self):
        self.client = MongoClient("127.0.0.1", 27017)
        self.db = self.client.pytest

    def add(self, category_name):
        post = {
                "_id": str(uuid.uuid4()),
                "name": category_name,
                "created": datetime.datetime.utcnow()
                }

        category = self.db.category.insert_one(post)

        return category.inserted_id

    def get_by_name(self, category_name):
        return self.db.category.find_one({"name": category_name})

    def get_by_id(self, category_id):
        return self.db.category.find_one({"_id": category_id})

    def get_all(self):
        result = list(self.db.category.find({}))
        return result

    def delete_by_id(self, category_id):
        result = self.db.category.delete_one({"_id": category_id})
        return result.deleted_count


class Online(Resource):
    def get(self):
        return {'status': 'online'}


class CategoryId(Resource):
    def get(self, category_id):
        repository = CategoryRepository()
        return jsonify(repository.get_by_id(category_id))

    def delete(self, category_id):
        repository = CategoryRepository()
        return jsonify(repository.delete_by_id(category_id))


class CategoryName(Resource):
    def get(self, category_name):
        repository = CategoryRepository()
        return jsonify(repository.get_by_name(category_name))


class Category(Resource):
    def post(self):
        repository = CategoryRepository()
        args = parser.parse_args()
        return jsonify(repository.add(args['name']))

    def get(self):
        repository = CategoryRepository()
        return jsonify(repository.get_all())


class CategoryCreate(Resource):
    def post(self):
        repository = CategoryRepository()
        args = parser.parse_args()
        return jsonify(repository.add(args['name']))


app = Flask(__name__)
api = Api(app)

api.add_resource(Online, '/')
api.add_resource(Category, '/category')
api.add_resource(CategoryName, '/category/name/<category_name>')
api.add_resource(CategoryId, '/category/<category_id>')
parser = reqparse.RequestParser()
parser.add_argument('name')


if __name__ == '__main__':
    app.run(debug=True)

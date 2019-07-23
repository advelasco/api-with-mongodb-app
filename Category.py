from repository import CategoryRepository
from flask import jsonify
from flask_restful import Resource, Api, reqparse


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
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        return jsonify(repository.add(args['name']))

    def get(self):
        repository = CategoryRepository()
        return jsonify(repository.get_all())

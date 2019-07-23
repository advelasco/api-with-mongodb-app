from pymongo import MongoClient
import datetime
import uuid


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

import pymongo
from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.users.insert(
            {"username": data.username, "name": data.name, "email id": data.email, "password": hashed})
        print("uid id: ", id)

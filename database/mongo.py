from pymongo import MongoClient
from bson import ObjectId

def seed_books_if_needed(db):
    collection = db.books
    print(collection.count_documents({}))
    if collection.count_documents({}) == 0:
        books = [
            {"_id": ObjectId("67cc6e0583b5428b1b80d575"), "title": "Dudus-Prezydent we mgle", "author": "Jacek Gądek", "year": 2008, "quantity": 5},
            {"_id": ObjectId("67f2cdc5cb7f4bbf143d3846"), "title": "Konfident", "author": "Krzysztof Domaradzki", "year": 2010, "quantity": 10},
            {"_id": ObjectId("67f2cdc7cb7f4bbf143d3847"), "title": "Z punktu widzenia ziemniaka", "author": "Filip Zawada", "year": 2018, "quantity": 15},
        ]
        collection.insert_many(books)
        print("Books updated successfully")
    else:
        print("Books already exists")


def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client.library
        seed_books_if_needed(db)
        return db
    except Exception as e:
        print("Error: ", e)
        return None
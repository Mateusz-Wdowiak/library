from flask import Flask, render_template, request, jsonify
from database.mongo import get_db
from random import randint
from bson import ObjectId
app = Flask(__name__)
db = get_db()
collection = db.books

## rendering pages
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/releases")
def releases():
    return render_template('releases.html')

## books endpoints

@app.route("/api/books", methods=['POST'])
def create_book():
    data = request.json
    if not data:
        return jsonify({"error": "Bad request body"}), 400

    img_id = randint(1, 3)
    new_book = {"title": data["title"], "author": data["author"], "year": data["year"], "description": data["description"], "imgId": img_id}
    res = collection.insert_one(new_book)

    return jsonify({"message": "Book created successfully", "id": str(res.inserted_id)}), 201

@app.route("/api/books", methods=['GET'])
def get_all_books():
    books_list = list(collection.find())
    return jsonify({"books": books_list})

@app.route("/api/books/<int:id>", methods=['GET'])
def get_book(book_id):
    book = collection.find_one({"_id": ObjectId(book_id)})

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book)

@app.route("/api/books/<int:id>", methods=['PUT'])
def update_book(book_id):
    data = request.json
    if not data:
        return jsonify({"error": "Bad request body"}), 400

    collection.update_one({"_id": ObjectId(book_id)}, {"$set": data})
    return jsonify({"message": "Book updated successfully"}), 200

@app.route("/api/books/<int:id>", methods=['DELETE'])
def delete_book(book_id):
    collection.delete_one({"_id": ObjectId(book_id)})
    return jsonify({"message": "Book deleted successfully"}), 200


## TODO auth endpoints

if __name__ == '__main__':
    app.run(debug=True)

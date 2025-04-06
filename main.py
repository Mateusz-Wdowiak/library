from flask import Flask, render_template, request, jsonify
from database.mongo import get_db
from random import randint
from bson import ObjectId
app = Flask(__name__)
db = get_db()
collection = db.books



@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/releases.html")
def releases():
    return render_template('releases.html')

@app.route("/")
def home():
    return render_template('index.html')

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


@app.route("/api/books/<id>", methods=['GET'])
def get_book(id):
    try:
        if not ObjectId.is_valid(id):
            return jsonify({"error": "Invalid book ID"}), 400

        book = collection.find_one({"_id": ObjectId(id)})
        if not book:
            return jsonify({"error": "Book not found"}), 404

        book['_id'] = str(book['_id'])
        return jsonify(book)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/books/<string:id>", methods=['DELETE'])
def delete_book(id):
    collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Book deleted successfully"}), 200

@app.route("/api/books/<id>", methods=['PUT'])
def update_book(id):
    try:
        data = request.json
        if not data or 'quantity' not in data:
            return jsonify({"error": "Bad request body"}), 400

        if not ObjectId.is_valid(id):
            return jsonify({"error": "Invalid book ID"}), 400

        result = collection.update_one(
            {"_id": ObjectId(id)},
            {"$inc": {"quantity": data['quantity']}}
        )

        if result.modified_count == 0:
            return jsonify({"error": "Book not found or not modified"}), 404

        return jsonify({"message": "Book updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

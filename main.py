from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client.library
print("Połączenie z bazą danych udane!")


collection = db.books

# Przykład dodawania dokumentu do bazy danych
document = {
    "title": "Wielki Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genre": "Novel"
}

collection.insert_one(document)

print("Dokument dodany do kolekcji 'books'!")
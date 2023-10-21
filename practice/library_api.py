from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

class BookSchema(Schema):
    title = fields.Str(required=True, validate=lambda s: 3 <= len(s) <= 100)
    author = fields.Str(required=True, validate=lambda s: 3 <= len(s) <= 100)
    publishedDate = fields.Date(required=True)

book_schema = BookSchema()

@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = book_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # If validation passes, proceed to save the book or perform other actions
    return 'Book added successfully', 201

if __name__ == '__main__':
    app.run(port=3000)

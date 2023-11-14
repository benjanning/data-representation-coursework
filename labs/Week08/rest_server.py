# rest_server.py
# A RESTful API for books using Flask

from flask import Flask, url_for, request, redirect, abort, jsonify
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# A sample data array to store the books
books=[
{"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
{"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
{"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]

# A variable to keep track of the next available id
nextId=4

# A route for the root URL (/) that returns a simple message
@app.route('/')
def index():
    return "hello"

# A route for getting all books (GET /books)
# curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    # Return the data array in JSON format
    return jsonify(books)

# A route for finding a book by id (GET /books/{id})
# curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>')
def findById(id):
    # Filter the data array for an object that has a matching id
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    # If no object is found, return an empty object and a status code of 204 (no content)
    if len(foundBooks) == 0:
        return jsonify({}), 204
    # Otherwise, return the first (and only) object in JSON format
    return jsonify(foundBooks[0])

# A route for creating a new book (POST /books)
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" -H "content-type:application/json" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId
    # Check that the user posted a JSON object (return an error if they did not)
    if not request.json:
        abort(400)
    # Create an object with data in it, and store it in the data array
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    # Increment the nextId variable
    nextId += 1
    # Return the created object in JSON format
    return jsonify(book)

# A route for updating an existing book (PUT /books/{id})
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    # Find the object in the data array that needs to be updated
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    # If no object is found, return an empty object and a status code of 404 (not found)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    # Otherwise, get the first (and only) object
    currentBook = foundBooks[0]
    # If the attribute was uploaded, then update that attribute
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']
    # Return the updated object in JSON format
    return jsonify(currentBook)

# A route for deleting a book (DELETE /books/{id})
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    # Find the object you wish to delete and remove it from the data array
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    # If no object is found, return an empty object and a status code of 404 (not found)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])
    # Return a message indicating that the deletion was successful
    return jsonify({"done":True})

# Run the app in debug mode if the file is executed as the main program
if __name__ == "__main__":
    app.run(debug=True)

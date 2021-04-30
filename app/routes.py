from flask import request
from flask import Blueprint
from flask import jsonify
from app import db
from app.models.book import Book




books_bp = Blueprint("books", __name__, url_prefix="/books")

def is_int(value):
    try:
        return int(value)
    except ValueError:
        return False

@books_bp.route("/<book_id>", methods=["GET"])
def get_single_book(book_id):
    # try to find book with given ID 
    if not is_int(book_id):
        return {"Success": False ,
                "message": f"{book_id} must be an integer."}, 400
    book = Book.query.get(book_id)
    if book:
        return book.to_json(), 200
    return {"Succes": False, 
            "Book ID": "Book ID was not found"}, 404


@books_bp.route("", methods=["GET"])
def books_index():
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append(book.to_json())
    return jsonify(books_response, 200)

@books_bp.route("", methods=["POST"])
def books():
    request_body = request.get_json()
    new_book = Book(title = request_body['title'], description = request_body['description'])

    db.session.add(new_book)
    db.session.commit()

    return ({"Success": True, "Book ID": new_book.id}, 201)



# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods = ["GET"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response

# @hello_world_bp.route("/hello-world/JSON", methods = ["GET"])
# def hello_world_json():
#     return { "name": "PolliPayne", 
#             "message": "OHAI", 
#             "hobbies": "Eating Dumplings"}, 200

# @hello_world_bp.route("/broken-endpoint-with-broken-code")
# def broken_endpoint():
#     response_body = {"name": "Ada Lovelace", 
#                     "message": "hello", 
#                     "hobbies": ["fishing", "swimming", "smashing the patriarchy"]}
#     new_hobby = "Running Marathons"
#     response_body["hobbies"].append(new_hobby)
#     return response_body
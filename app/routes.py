from flask import request
from flask import Blueprint
from app import db
from app.models.book import Book



books_bp = Blueprint("books", __name__, url_prefix="/books")

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
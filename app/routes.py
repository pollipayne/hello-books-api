from types import new_class
from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods = ["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route("/hello-world/JSON", methods = ["GET"])
def hello_world_json():
    return { "name": "PolliPayne", 
            "message": "OHAI", 
            "hobbies": "Eating Dumplings"}, 200

@hello_world_bp.route("/broken-endpoint-with-broken-code")
def broken_endpoint():
    response_body = {"name": "Ada Lovelace", 
                    "message": "hello", 
                    "hobbies": ["fishing", "swimming", "smashing the patriarchy"]}
    new_hobby = "Running Marathons"
    response_body["hobbies"].append(new_hobby)
    return response_body
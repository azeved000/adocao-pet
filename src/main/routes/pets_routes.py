from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest


from src.main.composer.pet_lister_composer import pet_lister_composer
from src.main.composer.pet_deleter_composer import pet_deleter_composer

pet__route_bp = Blueprint("pets_routes", __name__)

@pet__route_bp.route("/pets", methods=["GET"])
def list_pets():
    http_request = HttpRequest()
    view = pet_lister_composer()
    
    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pet__route_bp.route("/pets/<name>", methods=['DELETE'])
def deleter_pet(name):
    http_request = HttpRequest(param={ "name": name })
    view = pet_deleter_composer()

    http_response = view.handle(http_request)
    return jsonify(http_response.body), http_response.status_code
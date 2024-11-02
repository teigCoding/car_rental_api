from flask import Blueprint, request, jsonify
from neo4j_service import Neo4jService  # Import Neo4jService from the same directory as app.py

car_bp = Blueprint('car', __name__)

# Initialize the Neo4j connection
neo4j_service = Neo4jService("bolt://localhost:7687", "neo4j", "password")  # Replace with your credentials

@car_bp.route('/cars', methods=['POST'])
def add_car():
    car_data = request.get_json()
    car = neo4j_service.create_car(car_data)
    return jsonify({"message": "Car added", "car": car}), 201

@car_bp.route('/cars', methods=['GET'])
def get_cars():
    cars = neo4j_service.get_all_cars()
    return jsonify({"cars": cars})

@car_bp.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = neo4j_service.get_car_by_id(car_id)
    if car:
        return jsonify(car), 200
    else:
        return jsonify({"error": "Car not found"}), 404

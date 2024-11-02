from flask import Blueprint, request, jsonify
from config import driver

rental_bp = Blueprint('rental', __name__, url_prefix='/rental')

# Order Car
@rental_bp.route('/order-car', methods=['POST'])
def order_car():
    customer_id = request.json.get('customer_id')
    car_id = request.json.get('car_id')

    if not customer_id or not car_id:
        return jsonify(error="Missing customer_id or car_id"), 400

    with driver.session() as session:
        # Check if the customer already has a booked car
        existing_booking = session.run(
            """
            MATCH (c:Customer {id: $customer_id})-[:BOOKED]->(car:Car)
            RETURN car
            """,
            customer_id=customer_id
        ).single()
        
        if existing_booking:
            return jsonify(error="Customer already has a booked car"), 400

        # Book the car for the customer if it's available
        result = session.run(
            """
            MATCH (car:Car {id: $car_id, status: 'available'})
            MATCH (customer:Customer {id: $customer_id})
            SET car.status = 'booked'
            CREATE (customer)-[:BOOKED]->(car)
            RETURN car
            """,
            customer_id=customer_id,
            car_id=car_id
        ).single()

        if not result:
            return jsonify(error="Car is not available or does not exist"), 404
        
    return jsonify(message="Car booked successfully"), 200

# Cancel Order Car
@rental_bp.route('/cancel-order-car', methods=['POST'])
def cancel_order_car():
    customer_id = request.json.get('customer_id')
    car_id = request.json.get('car_id')

    if not customer_id or not car_id:
        return jsonify(error="Missing customer_id or car_id"), 400

    with driver.session() as session:
        # Check if the booking exists
        booking = session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[:BOOKED]->(car:Car {id: $car_id})
            RETURN car
            """,
            customer_id=customer_id,
            car_id=car_id
        ).single()

        if not booking:
            return jsonify(error="No booking found for this customer and car"), 404

        # Remove booking and set car status to available
        session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[b:BOOKED]->(car:Car {id: $car_id})
            DELETE b
            SET car.status = 'available'
            """,
            customer_id=customer_id,
            car_id=car_id
        )

    return jsonify(message="Booking canceled, car is now available"), 200
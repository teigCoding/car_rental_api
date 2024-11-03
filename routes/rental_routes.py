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

# Rent Car
@rental_bp.route('/rent-car', methods=['POST'])
def rent_car():
    customer_id = request.json.get('customer_id')
    car_id = request.json.get('car_id')

    if not customer_id or not car_id:
        return jsonify(error="Missing customer_id or car_id"), 400

    with driver.session() as session:
        # Check if there is an existing booking for the customer and car
        booking = session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[:BOOKED]->(car:Car {id: $car_id})
            RETURN car
            """,
            customer_id=customer_id,
            car_id=car_id
        ).single()

        if not booking:
            return jsonify(error="Customer does not have a booking for this car"), 404

        # Change the status from booked to rented
        session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[b:BOOKED]->(car:Car {id: $car_id})
            DELETE b
            SET car.status = 'rented'
            CREATE (customer)-[:RENTED]->(car)
            """,
            customer_id=customer_id,
            car_id=car_id
        )

    return jsonify(message="Car rented successfully"), 200

# Return Car
@rental_bp.route('/return-car', methods=['POST'])
def return_car():
    customer_id = request.json.get('customer_id')
    car_id = request.json.get('car_id')
    car_status = request.json.get('status')  # Expected values: "available" or "damaged"

    if not customer_id or not car_id or not car_status:
        return jsonify(error="Missing customer_id, car_id, or status"), 400

    with driver.session() as session:
        # Check if there is an active rental
        rental = session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[:RENTED]->(car:Car {id: $car_id})
            RETURN car
            """,
            customer_id=customer_id,
            car_id=car_id
        ).single()

        if not rental:
            return jsonify(error="Customer does not have a rental for this car"), 404

        # Return the car and set its status to 'available' or 'damaged'
        session.run(
            """
            MATCH (customer:Customer {id: $customer_id})-[r:RENTED]->(car:Car {id: $car_id})
            DELETE r
            SET car.status = $car_status
            """,
            customer_id=customer_id,
            car_id=car_id,
            car_status=car_status
        )

    return jsonify(message=f"Car returned successfully, status set to {car_status}"), 200

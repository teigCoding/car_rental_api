from config import get_driver

# Function to create a Car node
def create_car(car_id, make, model, year, location, status='available'):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (c:Car {id: $car_id, make: $make, model: $model, year: $year, location: $location, status: $status})
            """,
            car_id=car_id, make=make, model=model, year=year, location=location, status=status
        )

# Function to create a Customer node
def create_customer(customer_id, name, age, address):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (cust:Customer {id: $customer_id, name: $name, age: $age, address: $address})
            """,
            customer_id=customer_id, name=name, age=age, address=address
        )

# Function to create an Employee node
def create_employee(employee_id, name, address, branch):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (e:Employee {id: $employee_id, name: $name, address: $address, branch: $branch})
            """,
            employee_id=employee_id, name=name, address=address, branch=branch
        )

# Function to book a car
def book_car(customer_id, car_id):
    with get_driver().session() as session:
        # Check if the car is available
        result = session.run(
            "MATCH (c:Car {id: $car_id, status: 'available'}) RETURN c", car_id=car_id
        )
        if not result.single():
            return False  # Car is not available

        # Create the booking relationship
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id}), (c:Car {id: $car_id})
            CREATE (cust)-[:BOOKED]->(c)
            SET c.status = 'booked'
            """,
            customer_id=customer_id, car_id=car_id
        )
        return True

# Function to cancel a car booking
def cancel_booking(customer_id, car_id):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id})-[r:BOOKED]->(c:Car {id: $car_id})
            DELETE r
            SET c.status = 'available'
            """,
            customer_id=customer_id, car_id=car_id
        )

# Function to rent a car
def rent_car(customer_id, car_id):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id})-[:BOOKED]->(c:Car {id: $car_id})
            SET c.status = 'rented'
            """,
            customer_id=customer_id, car_id=car_id
        )

# Function to return a car
def return_car(customer_id, car_id, status):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id})-[r:BOOKED]->(c:Car {id: $car_id})
            DELETE r
            SET c.status = $status
            """,
            customer_id=customer_id, car_id=car_id, status=status
        )

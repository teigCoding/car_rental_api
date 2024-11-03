from config import get_driver

# Create Car
def create_car(car_id, make, model, year, location, status='available'):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (c:Car {id: $car_id, make: $make, model: $model, year: $year, location: $location, status: $status})
            """,
            car_id=car_id, make=make, model=model, year=year, location=location, status=status
        )

# Read Car
def get_car(car_id):
    with get_driver().session() as session:
        result = session.run(
            """
            MATCH (c:Car {id: $car_id})
            RETURN c
            """,
            car_id=car_id
        )
        return result.single()

# Update Car
def update_car(car_id, updates):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (c:Car {id: $car_id})
            SET c += $updates
            """,
            car_id=car_id, updates=updates
        )

# Delete Car
def delete_car(car_id):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (c:Car {id: $car_id})
            DELETE c
            """,
            car_id=car_id
        )

# Create Customer
def create_customer(customer_id, name, age, address):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (cust:Customer {id: $customer_id, name: $name, age: $age, address: $address})
            """,
            customer_id=customer_id, name=name, age=age, address=address
        )

# Read Customer
def get_customer(customer_id):
    with get_driver().session() as session:
        result = session.run(
            """
            MATCH (cust:Customer {id: $customer_id})
            RETURN cust
            """,
            customer_id=customer_id
        )
        return result.single()

# Update Customer
def update_customer(customer_id, updates):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id})
            SET cust += $updates
            """,
            customer_id=customer_id, updates=updates
        )

# Delete Customer
def delete_customer(customer_id):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (cust:Customer {id: $customer_id})
            DELETE cust
            """,
            customer_id=customer_id
        )

# Create Employee
def create_employee(employee_id, name, address, branch):
    with get_driver().session() as session:
        session.run(
            """
            CREATE (e:Employee {id: $employee_id, name: $name, address: $address, branch: $branch})
            """,
            employee_id=employee_id, name=name, address=address, branch=branch
        )

# Read Employee
def get_employee(employee_id):
    with get_driver().session() as session:
        result = session.run(
            """
            MATCH (e:Employee {id: $employee_id})
            RETURN e
            """,
            employee_id=employee_id
        )
        return result.single()

# Update Employee
def update_employee(employee_id, updates):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (e:Employee {id: $employee_id})
            SET e += $updates
            """,
            employee_id=employee_id, updates=updates
        )

# Delete Employee
def delete_employee(employee_id):
    with get_driver().session() as session:
        session.run(
            """
            MATCH (e:Employee {id: $employee_id})
            DELETE e
            """,
            employee_id=employee_id
        )

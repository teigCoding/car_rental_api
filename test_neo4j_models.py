from models.neo4j_models import (
    create_car, create_customer, create_employee,
    get_car, get_customer, get_employee,
    update_car, update_customer, update_employee,
    delete_car, delete_customer, delete_employee
)
import requests
import time

BASE_URL = "http://localhost:5001/rental"

def send_post_request(endpoint, payload):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.post(url, json=payload)
    print(f"{endpoint}: {response.status_code} - {response.json()}")
    return response

if __name__ == "__main__":
    # Step 1: Create nodes in Neo4j
    create_car(6, "BMW", "Series 5", 2021, "NYC", "available")
    create_car(5, "Toyota", "Camry", 2021, "NYC", "available")
    create_customer(201, "John Doe", 30, "123 Elm St")
    create_customer(202, "Marius Skjegletoft", 30, "122 Elm St")
    create_employee(301, "Alice Smith", "456 Pine St", "Downtown")
    create_employee(302, "Petter Smugle", "454 Pine St", "Downtown")
    print("Created Car, Customer, and Employee nodes.")

    # Step 2: Order cars
    send_post_request("order-car", {"customer_id": 201, "car_id": 6})
    send_post_request("order-car", {"customer_id": 202, "car_id": 5})
    time.sleep(1)

    # Step 3: Cancel a booking
    send_post_request("cancel-order-car", {"customer_id": 201, "car_id": 6})
    time.sleep(1)

    # Step 4: Re-book the car
    send_post_request("order-car", {"customer_id": 201, "car_id": 6})
    time.sleep(1)

    # Step 5: Rent the car
    send_post_request("rent-car", {"customer_id": 201, "car_id": 6})
    time.sleep(1)

    # Step 6: Return the car as available
    send_post_request("return-car", {"customer_id": 201, "car_id": 6, "status": "available"})
    time.sleep(1)

    # Step 7: Return a car as damaged
    send_post_request("order-car", {"customer_id": 201, "car_id": 6})  # Re-book for testing
    send_post_request("rent-car", {"customer_id": 201, "car_id": 6})   # Rent the car
    send_post_request("return-car", {"customer_id": 201, "car_id": 6, "status": "damaged"})
    time.sleep(1)

    # Additional Testing of nodes
    print("\n--- Additional Testing of Nodes ---\n")

    # Create a new set of nodes
    create_car(1, "Toyota", "Camry", 2021, "NYC", "available")
    create_customer(101, "Jane Doe", 28, "456 Maple St")
    create_employee(303, "Bob Johnson", "789 Cedar St", "Midtown")

    # Read nodes
    print("Car:", get_car(1))
    print("Customer:", get_customer(101))
    print("Employee:", get_employee(303))

    # Update nodes
    update_car(1, {"status": "rented"})
    update_customer(101, {"address": "789 Oak St"})
    update_employee(303, {"branch": "Uptown"})
    
    # Display updated nodes
    print("Updated Car:", get_car(1))
    print("Updated Customer:", get_customer(101))
    print("Updated Employee:", get_employee(303))

    # Delete nodes
    delete_car(1)
    delete_customer(101)
    delete_employee(303)

    print("\nCompleted all tests.")
    time.sleep(1)

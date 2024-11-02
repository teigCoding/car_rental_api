import requests
import json

BASE_URL = "http://localhost:5001/rental"

# Helper function to print formatted responses
def print_response(endpoint, response):
    print(f"Endpoint: {endpoint}")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}\n")

# Test the 'order-car' endpoint
def test_order_car():
    url = f"{BASE_URL}/order-car"
    payload = {
        "customer_id": "customer1",
        "car_id": "car1"
    }
    response = requests.post(url, json=payload)
    print_response("order-car", response)

# Test the 'cancel-order-car' endpoint
def test_cancel_order_car():
    url = f"{BASE_URL}/cancel-order-car"
    payload = {
        "customer_id": "customer1",
        "car_id": "car1"
    }
    response = requests.post(url, json=payload)
    print_response("cancel-order-car", response)

# Test the 'rent-car' endpoint
def test_rent_car():
    url = f"{BASE_URL}/rent-car"
    payload = {
        "customer_id": "customer1",
        "car_id": "car1"
    }
    response = requests.post(url, json=payload)
    print_response("rent-car", response)

# Test the 'return-car' endpoint
def test_return_car():
    url = f"{BASE_URL}/return-car"
    payload = {
        "customer_id": "customer1",
        "car_id": "car1",
        "status": "available"  # Can also test with "damaged"
    }
    response = requests.post(url, json=payload)
    print_response("return-car", response)

# Run all tests
if __name__ == "__main__":
    print("Testing Car Rental API Endpoints:\n")
    test_order_car()
    test_cancel_order_car()
    test_rent_car()
    test_return_car()

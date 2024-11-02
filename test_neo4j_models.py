from models.neo4j_models import create_car, create_customer, create_employee, book_car, cancel_booking, rent_car, return_car

# Test creating nodes
def test_create_nodes():
    create_car(1, "Toyota", "Camry", 2021, "NYC", "available")
    create_customer(101, "John Doe", 30, "123 Elm St")
    create_employee(201, "Alice Smith", "456 Pine St", "Downtown")
    print("Created Car, Customer, and Employee nodes.")

def test_order_car():
    url = f"{BASE_URL}/order-car"
    payload = {
        "customer_id": "101",
        "car_id": "1"
    }
    response = requests.post(url, json=payload)
    print_response("order-car", response)

# Test booking a car
def test_book_car():
    success = book_car(101, 1)
    if success:
        print("Car booked successfully.")
    else:
        print("Car booking failed (car might not be available).")

# Test canceling a booking
def test_cancel_booking():
    cancel_booking(101, 1)
    print("Canceled car booking.")

# Test renting a car
def test_rent_car():
    rent_car(101, 1)
    print("Car rented.")

# Test returning a car
def test_return_car():
    return_car(101, 1, "available")  # Change to "damaged" to test different statuses
    print("Car returned and status updated.")

# Run the tests
if __name__ == "__main__":
    test_create_nodes()     # Create the initial nodes
    test_book_car()         # Attempt to book the car
    test_cancel_booking()   # Cancel the booking
    test_book_car()         # Book again to test renting
    test_rent_car()         # Rent the car
    test_return_car()       # Return the car and update status

# Car Rental Service API

This is a Flask based API for managing a car rental service with data stored in a Neo4j database.

## Features

- **CRUD Operations**: Create, read, update, and delete `Cars`, `Customers`, and `Employees`.
- **Rental Management**:
  - **Order a Car**: Book a car for a customer.
  - **Cancel a Booking**: Cancel a car booking.
  - **Rent a Car**: Rent a car that was previously booked.
  - **Return a Car**: Return a rented car and update its status (`available` or `damaged`).

## Technologies Used

- **Flask**: Backend framework for handling HTTP requests and routing.
- **Neo4j**: Graph database to store and manage cars, customers, and employee data.
- **Requests**: Python library for testing endpoints by sending HTTP requests.

## Prerequisites

- **Python 3.x**
- **Neo4j**: Ensure Neo4j is installed and running on `bolt://localhost:7687`.
- **pip**: Python package installer.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/teigCoding/car_rental_api.git
    cd car_rental_api
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Neo4j Database**:
   Ensure your Neo4j database is running and accessible. Modify `config.py` if necessary with your Neo4j credentials.

4. **Run the Flask Application**:
    ```bash
    python app.py
    ```
   The API should now be accessible at `http://localhost:5001`.

## Project Structure

- **app.py**: Main application file to start the Flask server.
- **config.py**: Configuration file for setting up the Neo4j driver.
- **neo4j_models.py**: Contains functions to interact with the Neo4j database (create, read, update, delete).
- **neo4j_service.py**: Service class for Neo4j connection management.
- **routes/**: Contains route files for handling API endpoints (`rental_routes`).
- **test_neo4j_models.py**: Script to test the API endpoints by simulating different operations.

## Endpoints

| Endpoint               | Method | Description                                      |
|------------------------|--------|--------------------------------------------------|
| `/rental/order-car`    | POST   | Book a car for a customer.                       |
| `/rental/cancel-order-car` | POST   | Cancel a car booking for a customer.              |
| `/rental/rent-car`     | POST   | Rent a car that was booked for a customer.       |
| `/rental/return-car`   | POST   | Return a rented car and update its status.       |

### Example Requests

- **Order a Car**:
    ```json
    POST /rental/order-car
    {
      "customer_id": 201,
      "car_id": 6
    }
    ```

- **Return a Car (damaged)**:
    ```json
    POST /rental/return-car
    {
      "customer_id": 201,
      "car_id": 6,
      "status": "damaged"
    }
    ```

## Testing

The `test_neo4j_models.py` script includes automated tests for each endpoint:

1. **Run the API Server**:
    Ensure the Flask server is running:
    ```bash
    python app.py
    ```

2. **Run the Test Script**:
    In a new terminal window, run:
    ```bash
    python test_neo4j_models.py
    ```

   This script will create test data, perform various booking and rental operations, and print the results to the console.

## Requirements

See `requirements.txt` for the full list of dependencies:
- **Flask**: For building the API.
- **Neo4j**: For database connection.
- **Requests**: For testing HTTP endpoints.

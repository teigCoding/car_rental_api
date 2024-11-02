from flask import Flask
from routes.car_routes import car_bp        # Import the car routes
from routes.customer_routes import customer_bp  # Import the customer routes
from routes.employee_routes import employee_bp  # Import the employee routes

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(car_bp)       # Register the car blueprint
app.register_blueprint(customer_bp)  # Register the customer blueprint
app.register_blueprint(employee_bp)  # Register the employee blueprint

@app.route('/')
def home():
    return "Here we can see out the page."

if __name__ == '__main__':
    app.run(debug=True)

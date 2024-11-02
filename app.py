from flask import Flask
from routes.car_routes import car_bp
from routes.customer_routes import customer_bp
from routes.employee_routes import employee_bp
from neo4j_service import Neo4jService

app = Flask(__name__)

# Initialize Neo4j Service
neo4j_service = Neo4jService("bolt://localhost:7687", "neo4j", "neo4j")  # Replace with your credentials

# Register the blueprints
app.register_blueprint(car_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(employee_bp)

@app.route('/')
def home():
    return "Welcome to the Car Rental Service API!"

# Close the Neo4j connection when the app context is torn down
@app.teardown_appcontext
def close_neo4j_connection(exception=None):
    neo4j_service.close()

if __name__ == '__main__':
    app.run(debug=True)

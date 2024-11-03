from flask import Flask
from routes.rental_routes import rental_bp
from config import get_driver

app = Flask(__name__)

neo4j_driver = get_driver()

app.register_blueprint(car_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(rental_bp)


@app.route('/')
def home():
    return "Welcome to the Car Rental Service API!"

@app.teardown_appcontext
def close_neo4j_connection(exception=None):
    neo4j_driver.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)

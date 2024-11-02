from flask import Flask
from routes.car_routes import car_bp  # Import the car routes

app = Flask(__name__)
app.register_blueprint(car_bp)  # Register the car blueprint with the app

@app.route('/')
def home():
    return "Here we can see out page!"

if __name__ == '__main__':
    app.run(debug=True)

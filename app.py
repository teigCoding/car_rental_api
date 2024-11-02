from flask import Flask
# Import the routes
from routes.car_routes import car_bp        
from routes.customer_routes import customer_bp  
from routes.employee_routes import employee_bp  

app = Flask(__name__)

# Register the blueprints
app.register_blueprint(car_bp)       
app.register_blueprint(customer_bp) 
app.register_blueprint(employee_bp)  

@app.route('/')
def home():
    return "Here we can see out the page."

if __name__ == '__main__':
    app.run(debug=True)

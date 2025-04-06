from flask import Flask
from flask_cors import CORS
from .controllers.doctor_controller import doctor_blueprint
from .controllers.appointment_controller import appointment_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(doctor_blueprint, url_prefix='/api/v1')
    app.register_blueprint(appointment_blueprint, url_prefix='/api/v1')
    
    return app
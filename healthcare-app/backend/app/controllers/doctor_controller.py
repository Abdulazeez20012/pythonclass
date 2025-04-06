from flask import Blueprint, jsonify
from ..services.doctor_service import DoctorService

doctor_blueprint = Blueprint('doctor', __name__)

@doctor_blueprint.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = DoctorService.get_all_doctors()
    return jsonify([doctor.to_dict() for doctor in doctors])

@doctor_blueprint.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = DoctorService.get_doctor_by_id(doctor_id)
    if not doctor:
        return jsonify({'error': 'Doctor not found'}), 404
    return jsonify(doctor.to_dict())
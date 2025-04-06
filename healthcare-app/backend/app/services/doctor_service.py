from ..models.doctor import Doctor

class DoctorService:
    @staticmethod
    def get_all_doctors():
        return Doctor.query.all()
    
    @staticmethod
    def get_doctor_by_id(doctor_id):
        return Doctor.query.get(doctor_id)
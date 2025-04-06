import ApiService from './services/ApiService';
import DoctorController from './controllers/DoctorController';
import AppointmentController from './controllers/AppointmentController';

document.addEventListener('DOMContentLoaded', () => {
    const apiService = new ApiService();
    const doctorController = new DoctorController(apiService);
    const appointmentController = new AppointmentController(apiService, doctorController);
    
    doctorController.loadDoctors();
});
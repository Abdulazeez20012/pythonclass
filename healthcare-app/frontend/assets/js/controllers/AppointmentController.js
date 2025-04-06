class AppointmentController {
    constructor(apiService, doctorController) {
        this.apiService = apiService;
        this.doctorController = doctorController;
        this.selectedDoctor = null;
        this.selectedDate = null;
        this.selectedTime = null;
        this.availableSlots = [];

        this.domElements = {
            calendar: document.getElementById('calendar'),
            timeSlots: document.getElementById('timeSlots'),
            bookingSummary: document.getElementById('bookingSummary'),
            confirmBookingBtn: document.getElementById('confirmBookingBtn'),
            summaryDoctor: document.getElementById('summaryDoctor'),
            summaryDate: document.getElementById('summaryDate'),
            summaryTime: document.getElementById('summaryTime'),
            confirmationModal: document.getElementById('confirmationModal'),
            closeModalBtn: document.getElementById('closeModalBtn')
        };

        this.initEventListeners();
    }

    initEventListeners() {
        this.domElements.confirmBookingBtn.addEventListener('click', () => this.bookAppointment());

        this.domElements.closeModalBtn.addEventListener('click', () => this.closeModal());

        document.addEventListener('doctorSelected', (e) => {
            this.onDoctorSelected(e.detail);
        });
    }

    /**
     * @param {Object} doctor - Selected doctor object
     */
    async onDoctorSelected(doctor) {
        this.selectedDoctor = doctor;
        this.renderSelectedDoctor();
        await this.loadAvailableDates(doctor.id);
    }

   
    renderSelectedDoctor() {
        const selectedDoctorDiv = document.getElementById('selectedDoctor');
        selectedDoctorDiv.innerHTML = `
            <div class="flex items-center space-x-4">
                <div class="w-16 h-16 bg-gray-200 rounded-full flex items-center justify-center">
                    <i class="fas fa-user-md text-2xl text-gray-500"></i>
                </div>
                <div>
                    <h4 class="font-semibold">${this.selectedDoctor.name}</h4>
                    <p class="text-sm text-gray-600">${this.selectedDoctor.specialization}</p>
                </div>
            </div>
        `;
        selectedDoctorDiv.classList.remove('hidden');
        document.getElementById('changeDoctorBtn').classList.remove('hidden');
    }

    /**
     * @param {number} doctorId - ID of the selected doctor
     */
    async loadAvailableDates(doctorId) {
        try {
            const response = await this.apiService.get(`/doctors/${doctorId}/availability`);
            this.generateCalendar(response.data.available_dates);
        } catch (error) {
            console.error('Error loading available dates:', error);
            this.showError('Failed to load available dates. Please try again.');
        }
    }

    /**
     * @param {Array} availableDates - Array of available dates
     */
    generateCalendar(availableDates) {
        this.domElements.calendar.innerHTML = '';
        
        const dates = availableDates.map(dateStr => new Date(dateStr));
        
        dates.forEach(date => {
            const dayElement = document.createElement('div');
            dayElement.className = 'calendar-day';
            dayElement.textContent = date.getDate();
            
            dayElement.addEventListener('click', () => {
                this.onDateSelected(date);
                document.querySelectorAll('.calendar-day').forEach(el => {
                    el.classList.remove('selected');
                });
                dayElement.classList.add('selected');
            });
            
            this.domElements.calendar.appendChild(dayElement);
        });
    }

    /**
     * @param {Date} date - Selected date
     */
    async onDateSelected(date) {
        this.selectedDate = date;
        await this.loadAvailableTimes(this.selectedDoctor.id, date);
        this.updateBookingSummary();
    }

    /**
     * @param {number} doctorId - ID of the selected doctor
     * @param {Date} date - Selected date
     */
    async loadAvailableTimes(doctorId, date) {
        try {
            const dateStr = date.toISOString().split('T')[0];
            const response = await this.apiService.get(
                `/doctors/${doctorId}/availability/times?date=${dateStr}`
            );
            
            this.availableSlots = response.data.time_slots;
            this.renderTimeSlots();
        } catch (error) {
            console.error('Error loading available times:', error);
            this.showError('Failed to load available times. Please try again.');
        }
    }

    renderTimeSlots() {
        this.domElements.timeSlots.innerHTML = '';
        
        this.availableSlots.forEach(slot => {
            const timeElement = document.createElement('div');
            timeElement.className = 'time-slot';
            timeElement.textContent = slot.time;
            
            if (slot.booked) {
                timeElement.classList.add('booked');
            } else {
                timeElement.addEventListener('click', () => {
                    this.onTimeSelected(slot.time);
                    document.querySelectorAll('.time-slot').forEach(el => {
                        el.classList.remove('selected');
                    });
                    timeElement.classList.add('selected');
                });
            }
            
            this.domElements.timeSlots.appendChild(timeElement);
        });
    }

    /**
     * Handle time slot selection
     * @param {string} time - Selected time
     */
    onTimeSelected(time) {
        this.selectedTime = time;
        this.updateBookingSummary();
    }

    
    updateBookingSummary() {
        if (this.selectedDoctor && this.selectedDate && this.selectedTime) {
            this.domElements.summaryDoctor.textContent = this.selectedDoctor.name;
            this.domElements.summaryDate.textContent = this.selectedDate.toLocaleDateString('en-US', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
            this.domElements.summaryTime.textContent = this.selectedTime;
            this.domElements.bookingSummary.classList.remove('hidden');
        }
    }

    
    async bookAppointment() {
        if (!this.selectedDoctor || !this.selectedDate || !this.selectedTime) {
            this.showError('Please select doctor, date and time');
            return;
        }

        const appointmentData = {
            doctor_id: this.selectedDoctor.id,
            date: this.selectedDate.toISOString().split('T')[0],
            time: this.selectedTime,
            patient_id: this.getCurrentUserId() 
        };

        try {
            const response = await this.apiService.post('/appointments', appointmentData);
            this.showConfirmation(response.data);
            this.resetBookingFlow();
        } catch (error) {
            console.error('Error booking appointment:', error);
            this.showError('Failed to book appointment. Please try again.');
        }
    }

    /**
     * Show confirmation modal
     * @param {Object} appointment - Created appointment data
     */
    showConfirmation(appointment) {
        this.domElements.confirmationModal.classList.remove('hidden');
    }

    
    closeModal() {
        this.domElements.confirmationModal.classList.add('hidden');
    }

    resetBookingFlow() {
        this.selectedDate = null;
        this.selectedTime = null;
        this.domElements.bookingSummary.classList.add('hidden');
        this.domElements.calendar.innerHTML = '';
        this.domElements.timeSlots.innerHTML = '';
    }

    /**
     * @param {string} message - Error message
     */
    showError(message) {
        alert(message);
    }

    getCurrentUserId() {
        return 1; 
    }
}

export default AppointmentController;
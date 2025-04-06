class DoctorController {
    constructor(apiService) {
        this.apiService = apiService;
        this.doctors = [];
    }

    async loadDoctors() {
        try {
            this.doctors = await this.apiService.get('/doctors');
            this.renderDoctors();
        } catch (error) {
            console.error('Failed to load doctors:', error);
        }
    }

    renderDoctors() {
        const container = document.getElementById('doctorsList');
        container.innerHTML = this.doctors.map(doctor => `
            <div class="doctor-card">
                <h4>${doctor.name}</h4>
                <p>${doctor.specialization}</p>
                <span>${doctor.rating} | ${doctor.reviews_count} Reviews</span>
                <button class="book-btn" data-id="${doctor.id}">Book Appointment</button>
            </div>
        `).join('');

        document.querySelectorAll('.book-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.onDoctorSelected(parseInt(e.target.dataset.id));
            });
        });
    }

    onDoctorSelected(doctorId) {
        console.log('Doctor selected:', doctorId);
    }
}
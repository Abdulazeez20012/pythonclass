import random

class TeacherSchedule:
    def __init__(self):
        self.teachers = []
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.schedule = {day: None for day in self.days}

    def add_teacher(self, name, subject):
        self.teachers.append({"name": name, "subject": subject})

    def generate_schedule(self):
        random.shuffle(self.teachers)
        for day in self.days:
            if self.teachers:
                self.schedule[day] = self.teachers.pop(0)
            else:
                self.schedule[day] = None

    def get_schedule(self):
        return self.schedule

    def shuffle_schedule(self):
        self.teachers = list(filter(None, self.schedule.values()))
        self.generate_schedule()

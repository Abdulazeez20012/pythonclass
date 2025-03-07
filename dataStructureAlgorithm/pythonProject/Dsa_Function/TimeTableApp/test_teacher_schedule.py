import unittest
from Dsa_Function.TimeTableApp.teacher_schedule import TeacherSchedule

class TestTeacherSchedule(unittest.TestCase):
    def setUp(self):
        self.schedule = TeacherSchedule()

    def test_add_teacher(self):
        self.schedule.add_teacher("Mr. SK", "Python")
        self.assertEqual(len(self.schedule.teachers), 1)
        self.assertEqual(self.schedule.teachers[0]["name"], "Mr. SK")

    def test_generate_schedule_with_five_teachers(self):
        teachers = [
            ("Mr. SK", "Python"),
            ("Ms. Chibuzo", "java"),
            ("Mr. Chinedu", "JavaScript"),
            ("Ms. Ashley", "Design_Thinking"),
            ("Mr. Sk", "Jango")
        ]
        for name, subject in teachers:
            self.schedule.add_teacher(name, subject)
        self.schedule.generate_schedule()
        schedule = self.schedule.get_schedule()
        self.assertEqual(len(schedule), 5)
        self.assertIsNotNone(schedule["Monday"])

    def test_generate_schedule_with_less_than_five_teachers(self):
        teachers = [("Mr. SK", "Python"), ("Ms. Chibuzo", "java")]
        for name, subject in teachers:
            self.schedule.add_teacher(name, subject)
        self.schedule.generate_schedule()
        schedule = self.schedule.get_schedule()
        non_empty_days = sum(1 for day in schedule if schedule[day] is not None)
        self.assertEqual(non_empty_days, 2)

    def test_shuffle_schedule(self):
        teachers = [
            ("Mr. SK", "Python"),
            ("Ms. Chibuzo", "java"),
            ("Mr. Chinedu", "JavaScript"),
            ("Ms. Ashley", "Design_Thinking"),
            ("Mr. Sk", "Jango")
        ]
        for name, subject in teachers:
            self.schedule.add_teacher(name, subject)
        self.schedule.generate_schedule()
        original_schedule = self.schedule.get_schedule().copy()
        self.schedule.shuffle_schedule()
        new_schedule = self.schedule.get_schedule()
        self.assertNotEqual(original_schedule, new_schedule)

    def test_empty_schedule(self):
        self.schedule.generate_schedule()
        schedule = self.schedule.get_schedule()
        self.assertIsNone(schedule["Monday"])



if __name__ == "__main__":
    unittest.main()

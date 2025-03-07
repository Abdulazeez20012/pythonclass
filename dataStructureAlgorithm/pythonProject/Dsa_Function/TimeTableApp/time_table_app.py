from Dsa_Function.TimeTableApp.teacher_schedule import TeacherSchedule

def main():
    schedule = TeacherSchedule()

    while True:
        print("\nTeacher Schedule Application")
        print("1. Add Teacher")
        print("2. Generate Schedule")
        print("3. Show Schedule")
        print("4. Shuffle Schedule")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter teacher's name: ")
            subject = input("Enter teacher's subject: ")
            schedule.add_teacher(name, subject)
        elif choice == '2':
            schedule.generate_schedule()
            print("Schedule generated!")
        elif choice == '3':
            print_schedule(schedule.get_schedule())
        elif choice == '4':
            schedule.shuffle_schedule()
            print("Schedule shuffled!")
        elif choice == '5':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")


def print_schedule(schedule):
    print("\nWeekly Schedule:")
    for day, teacher in schedule.items():
        if teacher:
            print(f"{day}: {teacher['name']} ({teacher['subject']})")
        else:
            print(f"{day}: No teacher assigned")


if __name__ == "__main__":
    main()

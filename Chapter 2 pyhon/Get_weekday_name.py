def get_weekday_name(day_number):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= day_number <= 7:
        return weekdays[day_number - 1]
    else:
        return None

day_number = int(input("Enter a day number (1-7): "))

weekday_name = get_weekday_name(day_number)

if weekday_name:
    print("Weekday name:", weekday_name)
else:
    print("Invalid day number. Please enter a number between 1 and 7.")


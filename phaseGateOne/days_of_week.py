# Get today's day from the user
# Get the number of days after today for the future day
# switch case for days of the week
# Calculate the future day (wrap around using modulus)
# Get the names of the current and future days 
# Display the result

todays_day = int(input("Enter today's day : "))

days_elapsed = int(input("Enter the number of days elapsed since today: "))

match(todays_day):

   case  0:
	      print("Sunday")
   case  1:
	      print("Monday")
   case 2:
	      print("Tuesday")
   case 3:
	      print("Wednesday")
   case 4:
	      print("Thursday")
   case 5:
	      print("Friday")
   case 6:
	      print("Saturday")
   #default = ("it is not among the days number")

future_day = (todays_day + days_elapsed) % 7

today_name = todays_day(todays_day)
future_day_name = day_names(future_day)

print(f"Today is {today_name} and the future day is {future_day_name}")

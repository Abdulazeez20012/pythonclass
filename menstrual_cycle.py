# Welcome message
print("Welcome to the Menstrual Cycle checker!")

cycle_length = int(input("Enter the length of your menstrual cycle (in days): "))
period_length = int(input("Enter the length of your period (in days): "))
last_period_start = input("Enter the start date of your last period (in yyyy-mm-dd format): ")

date_parts = last_period_start.split("-")
year = int(date_parts[0])
month = int(date_parts[1])
day = int(date_parts[2])


ovulation_day = day + (cycle_length // 2)

if ovulation_day > 30:
    ovulation_day -= 30  
    month += 1  
    if month > 12:
        month = 1 
        year += 1  

safe_start_before = ovulation_day - 10
safe_end_before = ovulation_day - 7
safe_start_after = ovulation_day + 1
safe_end_after = ovulation_day + 6

next_period_start_day = day + cycle_length
if next_period_start_day > 30:
    next_period_start_day -= 30 
    month += 1  
    if month > 12:
        month = 1 
        year += 1  


print(f"\nOvulation Date: {year}-{month:02d}-{ovulation_day:02d}")
print(f"Safe Period: {year}-{month:02d}-{safe_start_before:02d} to {year}-{month:02d}-{safe_end_before:02d} "
      f"and {year}-{month:02d}-{safe_start_after:02d} to {year}-{month:02d}-{safe_end_after:02d}")
print(f"Next Period Start Date: {year}-{month:02d}-{next_period_start_day:02d}")

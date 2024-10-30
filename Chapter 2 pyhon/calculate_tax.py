def calculate_tax(earnings):
    if earnings <= 30000:
        return earnings * 0.15
    else:
        return 30000 * 0.15 + (earnings - 30000) * 0.20

citizens = ["John", "Alice", "Bob"]
earnings = []

for citizen in citizens:
    earnings.append(float(input(f"Enter earnings for {citizen}: ")))

for i in range(len(citizens)):
    tax = calculate_tax(earnings[i])
    print(f"{citizens[i]}'s total tax: ${tax:.2f}")


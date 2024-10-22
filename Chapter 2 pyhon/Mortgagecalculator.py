print("Welcome to FIN TECH where you can get your loan with ease and no collateral")

print("Let's calculate your monthly mortgage payment")

borrowed_amount = float(input("How much are you borrowing? ₦"))
interest_rate = float(input("What's the annual interest rate? (%) "))
repayment_years = int(input("How many years will you take to repay? "))

monthly_rate = (interest_rate / 100) / 12
total_months = repayment_years * 12

monthly_mortgage = round(borrowed_amount * monthly_rate * (1 + monthly_rate) ** total_months / ((1 + monthly_rate) ** total_months - 1))

print(f"Your monthly mortgage payment will be:₦{monthly_mortgage}")

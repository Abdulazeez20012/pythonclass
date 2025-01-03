def compound_interest_calculator():
    initial_investment = float(input("Enter initial investment: "))
    

    monthly_contribution = float(input("Enter monthly contribution (positive for deposit, negative for withdrawal): "))
    
  
    years = int(input("Enter length of time in years: "))
    

    interest_rate = float(input("Enter annual interest rate (as decimal, e.g., 5% = 0.05): "))
    
   
    variance = float(input("Enter interest rate variance range (e.g., 0.02 for ±2%): "))
    

    compound_frequency = int(input("Enter compound frequency (times per year, e.g., 1 for annually, 4 for quarterly): "))
    
   
    print("\nCalculating compound interest for the following scenarios:")
    for rate in [interest_rate - variance, interest_rate + variance]:
        total_amount = initial_investment
        monthly_rate = rate / compound_frequency
        months = years * 12
        
        for i in range(months):
            total_amount += monthly_contribution 
            if i % (12 // compound_frequency) == 0:  
                total_amount *= (1 + monthly_rate)
        
        print(f"Estimated amount at {rate * 100:.2f}% interest: {total_amount:.2f}")

compound_interest_calculator()

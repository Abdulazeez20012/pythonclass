def compound_interest_calculator():
    initial_investment = float(input("Enter initial investment: "))
    

    monthly_contribution = float(input("Enter monthly contribution:  "))
    
  
    years = int(input("Enter length of time in years: "))
    

    interest_rate = float(input("Enter annual interest rate: "))
    
   
    variance = float(input("Enter interest rate variance range: "))
    

    compound_frequency = int(input("Enter compound frequency: "))
    
   
    print("\nCalculating compound interest:")
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

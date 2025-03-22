symptoms = ["fever", "cough", "headache", "sore throat", "body pain", "fatigue", "shortness of breath"]


print("Please enter the symptoms you are experiencing (type 'done' to finish):")


reported_symptoms = []


for symptom in symptoms:
    user_input = input(f"Do you have {symptom}? (yes/no): ").strip().lower()
    
    if user_input == "yes":
        reported_symptoms.append(symptom)
    elif user_input == "no":
        continue
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("\nBased on the symptoms you've reported, here are some possibilities:")

if "fever" in reported_symptoms and "cough" in reported_symptoms:
    print("You might have the flu or a cold. Please consult a doctor.")
elif "shortness of breath" in reported_symptoms and "fatigue" in 

reported_symptoms:
    print("You might be experiencing symptoms of respiratory issues. Please consult a doctor immediately.")

elif "headache" in reported_symptoms and "sore throat" in 

reported_symptoms:
    print("It could be a mild viral infection. Take care and hydrate well.")
elif len(reported_symptoms) == 0:
    print("No symptoms reported. You seem to be feeling fine!")
else:
    print("Please monitor your symptoms. If they persist, see a healthcare professional.")

#
print("\nThank you for using the medical checker. Stay safe!")

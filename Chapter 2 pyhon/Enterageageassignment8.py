age = int(input("Enter your age: "))

max_heart_rate = 220 - age

target_min = max_heart_rate * 0.5
target_max = max_heart_rate * 0.85

print("\nResults:")
print(f"Maximum Heart Rate: {max_heart_rate} beats per minute")
print(f"Target Heart Rate Range: {target_min:.0f} 
{target_max:.0f} beats per minute"))
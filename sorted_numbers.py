numbers = [2, 2, 1, 3, 5, 5]

counter_dict = {}

for number in numbers:
    if number in counter_dict:
        counter_dict[number] += 1
    else:
        counter_dict[number] = 1

print("{")

for key, value in counter_dict.items():
    print(f'\t"{key}" : {value}')

print("}")

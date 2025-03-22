def extract_numbers_from_mixed_list(input_list):
    return [x for x in input_list if (lambda s: s.isdigit())(x)]

input_list = ['abc123def456',"hello","987","ii"]
output_list = extract_numbers_from_mixed_list(input_list)

print(output_list)

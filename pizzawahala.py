import math

def main():
   
    number_of_people = int(input("Enter the number of people: "))


    pizza_type = input("Enter the pizza type (Sapa size, Small Money, Big boys, Odogwu): ").strip()
    slices_per_box = 0
    price_per_box = 0

    
    if pizza_type.lower() == "sapa size":
        slices_per_box = 4
        price_per_box = 2500
    elif pizza_type.lower() == "small money":
        slices_per_box = 6
        price_per_box = 2900
    elif pizza_type.lower() == "big boys":
        slices_per_box = 8
        price_per_box = 4000
    elif pizza_type.lower() == "odogwu":
        slices_per_box = 12
        price_per_box = 5200
    else:
        print("Invalid pizza type. Please choose a valid pizza type.")
        return

   
    boxes_needed = math.ceil(number_of_people / slices_per_box)

   
    total_slices = boxes_needed * slices_per_box
    slices_left = total_slices - number_of_people

   
    total_price = boxes_needed * price_per_box

  
    print(f"Number of boxes of pizza to buy = {boxes_needed} boxes")
    print(f"Number of slices left over after serving = {slices_left} slices")
    print(f"Total Price = {total_price}")

if __name__ == "__main__":
    main()

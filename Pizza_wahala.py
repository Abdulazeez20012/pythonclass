import math

def pizza_order():

    SLICE_PER_BOX_ODOGWU = 12
    PRICE_PER_BOX_ODOGWU = 5200

    
    number_of_guests = int(input("Enter the number of guests: "))
    pizza_type = input("Enter the pizza type (e.g. Odogwu): ")

   
    if pizza_type.lower() == "odogwu":
        
        number_of_boxes = math.ceil(number_of_guests / SLICE_PER_BOX_ODOGWU)
        number_of_slices_left = (number_of_boxes * SLICE_PER_BOX_ODOGWU) - number_of_guests
        total_price = number_of_boxes * PRICE_PER_BOX_ODOGWU

      
    

def display_floor(floor):
    for row in floor:
        for cell in row:
            if cell == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def main():

    floor = [[0 for _ in range(20)] for _ in range(20)]
    
    
    x, y = 0, 0 
    pen_status = 1 
    direction = 0     
   
    commands = [5, 10, 3, 5, 12, 6, 9]
    
    i = 0
    while i < len(commands):
        command = commands[i]
        if command == 1: 
            pen_status = 1
        elif command == 2:  
            pen_status = 2
        elif command == 3:  
            direction = (direction + 1) % 4
        elif command == 4: 
            direction = (direction + 3) % 4
        elif command == 5: 
            steps = 10
            i += 1
            if i < len(commands):
                steps = commands[i]
            for _ in range(steps):
                if pen_status == 2:
                    floor[x][y] = 1 
                if direction == 0: x += 1  
                elif direction == 1: y += 1  
                elif direction == 2: x -= 1  
                elif direction == 3: y -= 1  
        elif command == 6:
            display_floor(floor)
        elif command == 9: 
            print("End of program")
            break
        i += 1

if __name__ == "__main__":
    main()

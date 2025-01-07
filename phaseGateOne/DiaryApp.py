def main():
    diary_ids = []
    diary_contents = [] 
    is_locked = False
    password = "A.z24434" 
    entry_count = 0

    while True:
        if is_locked:
            input_password = input("Enter password to unlock the diary: ")
            if input_password == password:
                is_locked = False
                print("Diary unlocked!")
            else:
                print("Incorrect password.")
                continue

        print("\nDiary Menu:")
        print("1. Add Entry")
        print("2. Update Entry")
        print("3. Delete Entry")
        print("4. Find Entry by ID")
        print("5. Lock Diary")
        print("6. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            
            if entry_count < 10:  
                entry_id = input("Enter ID for new entry: ")
                entry_content = input("Enter content for new entry: ")
                diary_ids.append(entry_id)
                diary_contents.append(entry_content)
                entry_count += 1
                print("Entry added successfully!")
            else:
                print("Diary is full! Cannot add more entries.")

        elif choice == 2:
          y
            update_id = input("Enter ID of the entry to update: ")
            found = False
            for i in range(entry_count):
                if diary_ids[i] == update_id:
                    new_content = input("Enter new content for the entry: ")
                    diary_contents[i] = new_content
                    found = True
                    print("Entry updated successfully!")
                    break
            if not found:
                print("Entry not found.")

        elif choice == 3:
            
            delete_id = input("Enter ID of the entry to delete: ")
            found = False
            for i in range(entry_count):
                if diary_ids[i] == delete_id:
                    diary_ids.pop(i)
                    diary_contents.pop(i)
                    entry_count -= 1
                    found = True
                    print("Entry deleted successfully!")
                    break
            if not found:
                print("Entry not found.")

        elif choice == 4:
           
            find_id = input("Enter ID of the entry to find: ")
            found = False
            for i in range(entry_count):
                if diary_ids[i] == find_id:
                    print(f"Entry found:\nID: {diary_ids[i]}\nContent: {diary_contents[i]}")
                    found = True
                    break
            if not found:
                print("Entry not found.")

        elif choice == 5:
           
            is_locked = True
            print("Diary locked!")

        elif choice == 6:
           
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

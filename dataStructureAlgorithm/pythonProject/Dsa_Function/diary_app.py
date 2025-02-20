from Dsa_Function.diaries import Diaries

def main():
    diaries = Diaries()
    diaries.create_diary(1)
    diary = diaries.get_diary(1)

    while True:
        print("\nDiary App")
        print("1. Login")
        print("2. Create Entry")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. View Entry")
        print("6. List Entries")
        print("7. Lock Diary")
        print("8. Unlock Diary")
        print("9. Find Entry by ID")
        print("10. Logout")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            password = input("Enter password: ")
            try:
                diary.login(password)
                print("Logged in successfully")
            except ValueError as e:
                print(e)

        elif choice == '2':
            if diary.is_logged_in:
                entry_id = int(input("Enter entry ID: "))
                title = input("Enter entry title: ")
                content = input("Enter entry content: ")
                try:
                    diary.entries.create_entry(entry_id, title, content)
                    print("Entry created successfully")
                except Exception as e:
                    print(e)
            else:
                print("Please login first")

        elif choice == '3':
            if diary.is_logged_in:
                entry_id = int(input("Enter entry ID: "))
                title = input("Enter new title: ")
                content = input("Enter new content: ")
                try:
                    diary.entries.update_entry(entry_id, title, content)
                    print("Entry updated successfully")
                except Exception as e:
                    print(e)
            else:
                print("Please login first")

        elif choice == '4':
            if diary.is_logged_in:
                entry_id = int(input("Enter entry ID to delete: "))
                try:
                    diary.entries.delete_entry(entry_id)
                    print("Entry deleted successfully")
                except Exception as e:
                    print(e)
            else:
                print("Please login first")

        elif choice == '5':
            if diary.is_logged_in:
                entry_id = int(input("Enter entry ID to view: "))
                try:
                    entry = diary.entries.view_entry(entry_id)
                    print(entry)
                except Exception as e:
                    print(e)
            else:
                print("Please login first")

        elif choice == '6':
            if diary.is_logged_in:
                entries = diary.entries.list_entries()
                for entry in entries:
                    print(entry)
            else:
                print("Please login first")

        elif choice == '7':
            diary.lock_diary()
            print("Diary locked")

        elif choice == '8':
            diary.unlock_diary()
            print("Diary unlocked")

        elif choice == '9':
            if diary.is_logged_in:
                entry_id = int(input("Enter entry ID to find: "))
                try:
                    entry = diary.entries.find_entry_by_id(entry_id)
                    print(entry)
                except Exception as e:
                    print(e)
            else:
                print("Please login first")

        elif choice == '10':
            diary.logout()
            print("Logged out")

        elif choice == '11':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

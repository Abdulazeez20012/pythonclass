from Dsa_Function.azBank.bank import Bank

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_pin_input(prompt):
    while True:
        pin = input(prompt).strip()
        if not (pin.isdigit() and len(pin) == 4):
            print("Invalid PIN. PIN must be exactly 4 digits.")
        else:
            return pin

def main():
    bank = Bank()

    while True:
        print("\n=== Welcome to the Bank App ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Close Account")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            first_name = input("Enter your first name: ").strip()
            last_name = input("Enter your last name: ").strip()
            pin = get_pin_input("Enter a 4-digit PIN: ")
            try:
                initial_deposit = get_float_input("Enter initial deposit amount: ")
            except ValueError:
                print("Invalid deposit amount.")
                continue

            try:
                account = bank.create_account(first_name, last_name, pin, )
                print("\nAccount created successfully!")
                print(f"Account Holder: {account.get_full_name()}")
                print(f"your Account Number is : {account.account_number}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            acc_num = input("Enter account number: ").strip()
            try:
                amount = get_float_input("Enter deposit amount: ")
                new_balance = bank.deposit(acc_num, amount)
                print(f"Deposit successful! New balance: {new_balance}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            acc_num = input("Enter account number: ").strip()
            try:
                amount = get_float_input("Enter withdrawal amount: ")
                new_balance = bank.withdraw(acc_num, amount)
                print(f"Withdrawal successful! New balance: {new_balance}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            acc_num = input("Enter account number: ").strip()
            try:
                balance = bank.check_balance(acc_num)
                print(f"Current balance: {balance}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            from_acc = input("Enter your account number: ").strip()
            to_acc = input("Enter recipient account number: ").strip()
            try:
                amount = get_float_input("Enter transfer amount: ")
                bank.transfer(from_acc, to_acc, amount)
                print("Transfer successful!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "6":
            acc_num = input("Enter account number to close: ").strip()
            try:
                bank.close_account(acc_num)
                print("Account closed successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "7":
            print("Thank you for using the Bank App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == '__main__':
    main()
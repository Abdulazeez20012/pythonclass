import re

import bcrypt
USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f"{username}:{hashed_password.decode('utf-8')}\n")

def register_user():
    while True:
        username = input('Enter your username: ')
        if not username:
            print('Username is required.')
            continue
        break

    password = input('Enter your password: ')

    while not re.fullmatch(r'\w{8,}', password):
        password = input('Enter your password: ')
        if not password:
            print('Password is required.')
            continue
        break

    while True:
        password_confirmation = input('Confirm your password: ')
        if not password_confirmation:
            print('Password is required.')
            continue
        break

    save_to_file(username, hash_password(password))

def validate_user(username, password):
    with open(USER_DETAILS, 'r') as file:
        details = file.read()
        for line in details.split(','):
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username:
                return bcrypt.checkpw(password.encode('utf-8'), stored_username.encode('utf-8'))

def login_user (username, password):
    username = input('Enter your username: ').strip()
    password = input('Enter your password: ').strip()
    while not re.fullmatch(r'\w{8,}', password):
        password = input('Enter your password: ')
    if validate_user(username, password):
        print("Logged in!")
    else:
        print("invalid Details")


def main():
    print( """"
    1 to register_user
    2 to login user
    3 to exit.""""")
    choice = input('Enter your choice: ')

    match choice:
        case '1':
            register_user()
        case '2':
            login_user()
        case '3':
            print("Thank you!")


main()

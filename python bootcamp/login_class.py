
import re
from datetime import datetime

class Login:
    def __init__(self):
        self.user_info = {}

    def is_valid_name(self, name):
        # Validate that the name contains only letters and is at least one character long
        regex = r'^[a-zA-Z]+$'
        return bool(re.match(regex, name))

    def is_valid_email(self, email):
        # Improved regex for email validation
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+(\.\w+)?$'
        return bool(re.match(regex, email))

    def is_valid_phone(self, phone):
        # Ensure the phone number is exactly 10 digits
        regex = r'^\d{10}$'
        return bool(re.match(regex, phone))

    def is_valid_dob(self, dob):
        # Validate the date of birth format YYYY-MM-DD
        try:
            datetime.strptime(dob, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def collect_user_info(self):
        name = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")

        if not self.is_valid_name(name):
            print("Invalid first name! It should contain only letters.")
            return None

        if not self.is_valid_name(lastname):
            print("Invalid last name! It should contain only letters.")
            return None

        if not self.is_valid_email(email):
            print("Invalid email address!")
            return None

        if not self.is_valid_phone(phone):
            print("Invalid phone number! It should be a 10 digit number.")
            return None

        if not self.is_valid_dob(dob):
            print("Invalid date of birth! It should be in the format YYYY-MM-DD.")
            return None

        self.user_info = {
            "name": name,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "dob": dob
        }
        return self.user_info

def main():
    print("Welcome to the Login System")
    login = Login()
    user_info = None

    while not user_info:
        user_info = login.collect_user_info()

    print("User information collected successfully.")
    print("Login successful!")
    print("Collected User Info:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()

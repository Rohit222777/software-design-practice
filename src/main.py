from user import User
from utils import validate_email

def main():
    name = input("Enter your name: ")
    email = input("Enter your email: ")

    if validate_email(email):
        user = User(name, email)
        print("User created successfully!")
        user.display()
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    main()

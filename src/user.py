# user.py
class User:
    """
    Represents a user in the system.
    Follows SRP: Only handles user-related data and behavior.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

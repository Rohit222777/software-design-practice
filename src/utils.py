# utils.py
import re

def validate_email(email):
    """
    Validates an email address using regex.
    Demonstrates code reusability (DRY principle).
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

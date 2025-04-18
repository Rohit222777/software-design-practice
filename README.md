# software-design-practice
Software Research and Practice Assignment for IT5016


##  Overview
This Python project demonstrates basic software design principles in action. It handles user input, email validation, and user creation using separate modules for better organization and maintainability.

##  Software Design Principles Applied

### 1. Single Responsibility Principle (SRP)
- `User` class only manages user data and display functionality.
- `utils.py` handles validation logic.
- `main.py` orchestrates the application.

### 2. DRY (Don’t Repeat Yourself)
- The email validation function is reused across the app.

### 3. Modularity & Separation of Concerns
- Code is organized into files (`main.py`, `user.py`, `utils.py`), each with a distinct purpose.

### 4. Open/Closed Principle
- You can extend the app by adding more validations without modifying existing code.

---

##  How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Rohit222777/software-design-practice.git

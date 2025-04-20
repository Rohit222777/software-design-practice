
# software-design-practice  
**Software Research and Practice Assignment for IT5016**

## Overview  
This Python project demonstrates fundamental software design principles through a simple user management system. It handles user input, email validation, and user creation by using separate modules to enhance code maintainability, readability, and scalability. The goal of this project is to showcase how proper software architecture can result in clean, reusable, and extensible code.

## Software Design Principles Applied  

### 1. Single Responsibility Principle (SRP)  
The SRP is followed well in this project. Each file and class has a distinct and singular purpose:  
- The `User` class in `user.py` is responsible solely for storing and displaying user data.  
- `utils.py` is used exclusively for validation logic, like checking if an email is valid.  
- `main.py` acts as the orchestrator of the application flow — gathering user input and using the other modules accordingly.  

This separation ensures that each module or class has only one reason to change, which is the essence of SRP.

### 2. Don’t Repeat Yourself (DRY)  
The DRY principle is reflected in the centralized implementation of validation logic. The email validation function is defined once in `utils.py` and reused wherever validation is required. This avoids code duplication and makes future updates (e.g., changes in the validation logic) easy and efficient.

### 3. Modularity & Separation of Concerns  
The application is modular, with a clear division of responsibilities across different files.  
- `main.py`: Entry point, handles program flow  
- `user.py`: Defines the `User` class  
- `utils.py`: Contains utility functions like validation  

This structure simplifies understanding, testing, and extending the application. Any developer can jump into one file and understand its role without needing to comprehend the entire codebase.

### 4. Open/Closed Principle  
The code demonstrates this principle reasonably well. For example, additional validations (such as username formatting or password strength) can be added to `utils.py` without changing the core application logic in `main.py` or the structure of the `User` class.

## Limitations and Areas for Improvement  

- **Violations of the Liskov Substitution Principle (LSP) and Interface Segregation Principle (ISP)**:  
  These principles are not addressed as there is no inheritance or interface-based structure in the current design.

- **Scalability and Flexibility Limitations**:  
  While modular, the application does not yet implement error handling or logging, which are essential for larger applications. Adding custom exception classes and a logging module would greatly enhance robustness and maintainability.

- **Tight Coupling in `main.py`**:  
  The current `main.py` file tightly couples input logic with application flow. In a more scalable design, these could be further separated — for example, by using a controller or service layer.

- **Testing**:  
  There are no unit tests or test strategy defined. This is a limitation from a design and maintainability standpoint. Adding a test suite would promote Test-Driven Development (TDD) and support the overall robustness of the system.

- **Hardcoded Input and Console Use**:  
  The system is currently built for interactive console use. To improve upon this, a user interface abstraction could be added, allowing the core logic to be reused in both command-line and graphical/web interfaces.

## How to Run  

1. Clone the repo:
   ```bash
   git clone https://github.com/Rohit222777/software-design-practice.git
   ```
2. Navigate into the project folder and run:
   ```bash
   python main.py
   ```

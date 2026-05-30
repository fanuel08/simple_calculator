# Basic Calculator Program

'''Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.'''

def get_valid_input():
    """Get and validate user input for two numbers and an operation."""
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter a mathematical operation (+, -, *, /): ").strip()
            
            # Validate operation
            if operation not in ["+", "-", "*", "/"]:
                print("Invalid operation. Please enter +, -, *, or /")
                continue
                
            return num1, num2, operation
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

def calculate(num1, num2, operation):
    """Perform the calculation based on the operation."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero")
            return None
        return num1 / num2

def main():
    """Main program logic."""
    num1, num2, operation = get_valid_input()
    result = calculate(num1, num2, operation)
    
    if result is not None:
        print(f"\n{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()

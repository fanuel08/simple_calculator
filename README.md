# Simple Calculator

A Python program that performs basic mathematical operations on user-provided numbers.

## Features

- **Addition** - Add two numbers together
- **Subtraction** - Subtract two numbers
- **Multiplication** - Multiply two numbers
- **Division** - Divide two numbers (with zero-division protection)
- **Input Validation** - Validates user input and re-prompts on errors
- **Error Handling** - Handles invalid operations and edge cases gracefully

## Requirements

- Python 3.x

## Usage

Run the program:

```bash
python PLP_python_assignment.py
```

### Example

```
Enter the first number: 10
Enter the second number: 5
Enter a mathematical operation (+, -, *, /): +

10.0 + 5.0 = 15.0
```

## Program Flow

1. The program prompts the user to enter two numbers
2. The user selects a mathematical operation (+, -, *, /)
3. The program validates all inputs
4. If inputs are invalid, the user is prompted to try again
5. The calculation is performed and the result is displayed
6. Division by zero is prevented with an error message

## Code Structure

- `get_valid_input()` - Handles user input and validation
- `calculate()` - Performs the mathematical operation
- `main()` - Orchestrates the program logic

## Error Handling

- **Invalid Numbers** - If non-numeric input is provided, the user is prompted to re-enter
- **Invalid Operation** - If an unsupported operation is entered, the user is prompted to choose from +, -, *, /
- **Division by Zero** - Prevents crashing and displays an error message

## Future Enhancements

- Add support for more operations (exponentiation, modulo, etc.)
- Implement a loop to perform multiple calculations
- Add a history of previous calculations
- Create a GUI interface

---

*Assignment: PLP Python Calculator*

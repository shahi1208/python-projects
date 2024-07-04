# python-projects

# [Simple Python Calculator-Beginner level](https://github.com/shahi1208/python-projects/blob/main/calculator.py)

This Python script implements a basic calculator with support for addition, subtraction, multiplication, and division operations. It handles input validation, ensuring the user enters valid operators and numbers. If division by zero is attempted, the program prompts the user to enter a new denominator.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`), with error handling for division by zero

## How It Works

1. **Functions for Operations:**
   - `add(a, b)`: Adds two numbers `a` and `b`.
   - `sub(a, b)`: Subtracts `b` from `a`.
   - `mul(a, b)`: Multiplies `a` by `b`.
   - `div(a, b)`: Divides `a` by `b`, with error handling for division by zero.

2. **Input Validation:**
   - The `oper(op)` function ensures the entered operator is valid by recursively prompting the user until a valid operator (`+`, `-`, `*`, `/`) is entered.

3. **User Interaction:**
   - The calculator starts with a welcome message and prompts the user to press 'Y' to start or 'X' to terminate.
   - After each calculation, it displays the result and prompts the user to continue (`Y`) or terminate (`X`).

4. **Error Handling:**
   - If the user attempts division with zero as the denominator, it prints an error message and prompts for a new value.

5. **Termination:**
   - The program terminates when the user inputs 'X' to exit the calculator.

## Example Usage

```plaintext
Welcome to my calculator. Press Y to start.

Press Y to continue. X to terminate.
X OR Y? Y

enter first value: 10

Available operators- ['+', '-', '*', '/']
enter an operator: +

enter second value: 5

15
Press Y to continue. X to terminate.
X OR Y? Y

enter first value: 12

Available operators- ['+', '-', '*', '/']
enter an operator: /
enter second value: 0

ZeroDivisionError: Denominator cannot be zero
Enter a new value for Denominator: 2

6.0
Press Y to continue. X to terminate.
X OR Y? X

calculator is closed.
```


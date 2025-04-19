# Simple Calculator Program

## Overview

This is a basic Python calculator script that allows users to perform two operations: **Addition** and **Subtraction**. The program runs in a loop until the user decides to exit.

## Features

- Menu-driven interface
- Performs addition and subtraction of two user-input numbers
- Clean function-based structure
- Loops until the user chooses to exit

## Functional Flow

### 1. Display Calculator Menu

The program begins by displaying a menu with options:

Welcome to Calculator

Choose one operation:

- Add

- Subtract

- Exit

### 2. Get User Choice

The user is prompted to select an operation by entering a number (1, 2, or 3).

### 3. Perform Calculation

Based on the selected option:

- **Add (1)**:
  - Prompts the user for two numbers.
  - Calculates and displays the sum.

- **Subtract (2)**:
  - Prompts the user for two numbers.
  - Calculates and displays the difference.

- **Exit (3)**:
  - Prints an exit message and stops the program.

### 4. User Input

The program collects two integers from the user for both addition and subtraction operations.

### 5. Looping

The calculator continues to run until the user selects **Exit (3)**.

## Function Breakdown

- `calculatorDisplay()`: Returns the calculator menu string.
- `calculatorFunction(user_choice)`: Handles the logic based on the user’s choice.
- `user_input()`: Prompts the user to enter two numbers.
- `addition(a, b)`: Returns the sum of two numbers.
- `subtraction(a, b)`: Returns the difference of two numbers.

## Example Interaction

Welcome to Calculator

Choose one operation:

- Add

- Subtract

- Exit

Select the operation: 1 Give two numbers on two lines Number 1 is: 10 Number 2 is: 5 The sum is: 15


## Exit Condition

The program exits when the user inputs `3`:

Exiting the calculator, bye bye!

---

This script is ideal for Python beginners to understand functions, user input handling, and control flow.

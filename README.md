# Python Assignments

This repository contains beginner-level Python programs.

## Assignment3_task_1: Factorial Calculation
- Prompts the user to enter an integer.
- Uses a 'for' loop to compute the factorial.
- Displays the result.
- Handles invalid input using try-except.

--- How It Works

- Factorial of a number n (written as n!) is:

- n! = n × (n - 1) × (n - 2) × ... × 1

- Example:
- 5! = 5 × 4 × 3 × 2 × 1 = 120

Code Example

try:
    n = int(input("Enter a number: "))
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"The factorial of {n} is: {factorial}")

except ValueError:
    print("Please enter a valid integer.")

## Assignment3_task_2: Using The MATH Module for Calculation
- This Python program performs three mathematical operations on a user-entered number:

- Square root
- Natural logarithm (base e)
- Sine (in radians)

- The program ensures the number entered is greater than 0 and handles invalid input using exception handling.

--- How IT Works

The program uses Python's built-in "math" module:

- 'math.sqrt(x)' → Returns the square root of x
- 'math.log(x)' → Returns the natural logarithm of x
- 'math.sin(x)' → Returns the sine of x (x must be in radians)

Example Code

import math

try:
    num = float(input("Enter a number greater than 0: "))

    if num <= 0:
        raise ValueError("Number must be greater than 0.")

    square_root = math.sqrt(num)
    natural_log = math.log(num)
    sine_value = math.sin(num)

    print("\nResults:")
    print("Square root:", square_root)
    print("Natural logarithm (base e):", natural_log)
    print("Sine (in radians):", sine_value)

except ValueError as ve:
    print("Error:", ve)

## Assignment2_task_1: Odd Even Checker
- Prompts the user to enter an integer.
- Checks if the number is divisible by 2. 
- Displays whether the number is Even or Odd.
- Handles invalid input gracefully (if included in your version).

--- How It Works

- A number is "even" if it is divisible by 2 (remainder = 0).
- A number is "odd" if it is not divisible by 2 (remainder ≠ 0).

The program uses the modulus operator '%' to determine the remainder.

Example logic:
- if num % 2 == 0:
      print("Even")
- else:
      print("Odd")

## Assignment2_task_2: Sum of numbers from 1 to 50
- Uses a 'for' loop to iterate through numbers 1 to 50.
- Adds each number to a running total.
- Prints the final sum.

--- How It Works

The program uses the built-in 'range()' function:
- total = 0
- for i in range(1, 51):
-    total += i
- print(f"The sum of the numbers in the range 1 to 50 is: {total}")

## Task 1: Basic Calculator
- Takes two numbers as input
- Performs addition, subtraction, multiplication, and division
- Displays the results

## Task 2: Name Greeting Program
- Takes first name and last name as input
- Combines them into a full name
- Prints a personalized greeting


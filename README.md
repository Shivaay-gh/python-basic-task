# Python Assignments

This repository contains beginner-level Python programs.

## tkinter: Calculator using tkinter
This program contains simple tkinter Calculator. It supports -
- Addition (+), subtraction (-), multiplication (*), and division (/)

---  How It Works

- The program uses a 'Calculator' class to manage the calculator logic.
- Button" for numbers (0–9), operators, equal, and clear are created.
- Clicking an operator stores the first number and the operator.
- Clicking "=" computes the result and displays it.
- Invalid operations show "ERROR" in the entry box.

---  Specification

- It's interface built with "Tkinter"
- Case-insensitive handling of numbers.
- Prevents crashes for invalid input or division by zero


## Assignment5_task_2: Write and Append data in a file
This Python program demonstrates basic file operations:
- Write user input to a file.
- Append additional text to the same file.
- Read and display the file content.

--- How It Works

1. Write mode ("w"): Saves the user's input to ''output.txt'.  
2. Append mode ("a"): Adds more content to the same file without overwriting.  
3. Read mode ("r"): Reads the content line by line and displays it.

Example code:

with open("output.txt", "w") as file:
-    file.write(user_input + "\n")

with open("output.txt", "a") as file:
 -   file.write(additional_data + "\n")

with open("output.txt", "r") as file:
 -   for line in file:
 -    print(line, end='') 



## Assignment5_task_1: Read a File and Handle Errors
This Python program reads the content of a file named "sample.txt" and prints each line with its line number.

Features:
- Reads a file line by line.
- Displays line numbers.
- Handles the case when the file does not exist.

--- How It Works

1. The program attempts to open "sample.txt" in read mode.
2. Each line is read and printed along with its line number.
3. If the file is missing, a "FileNotFoundError" is caught and an error message is displayed.

Example code:

- with open("sample.txt", 'r') as file:
-    for line_number, line in enumerate(file, start=1):
-       print(f"Line {line_number}: {line.strip()}")

## Assignment4_task_1: Students Marks Lookup
- This Python program allows you to look up a student's marks from a predefined dictionary.

Key features:
- Case-insensitive search (e.g., "alice", "ALICE", "Alice" all work)
- Handles missing records gracefully
- Displays marks with proper formatting.

## Assignment4_task_2: LIST SLICING & REVERSING
- This Python program demonstrates basic list operations:
- Extracting a subset of elements from a list
- Reversing the extracted elements

--- How It Works

A list of numbers from 1 to 10 is created:

- numbers = list(range(1, 11))
- first_five = numbers[:5]
- reversed_first_five = first_five[::-1]


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


try:
    n = int(input("Enter a number: "))

    factorial = 1

    for i in range(1, n+1):
     factorial *= i
     print(f"The Factorial of {n} is: {factorial}")

except ValueError:
    print("Please enter a valid integer.")


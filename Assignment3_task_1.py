def factorial(n):
    "calculate the factorial using recursion"
    if n < 0:
        raise ValueError("Number must be non zero.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


try:
    n = int(input("Enter a number: "))
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")
except ValueError as e:
    print("Error:", e)


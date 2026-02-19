import math

try:
    num = float(input("Enter a number: "))

    if num <= 0:
        raise ValueError("Number must be greater than 0.")

    square_root = math.sqrt(num)
    natural_logarithm = math.log(num)
    sine_value = math.sin(num)

    print("\nResult:")
    print("Square root of your number is: ", square_root)
    print("Natural logarithm of your number is: ", natural_logarithm)
    print("Sine value of your number is: ", sine_value)

except ValueError as ve:
    print("ERROR:", ve)

except Exception as e:
    print("An unexpected error occurred: ", e)

"""
when all the length of the sides of the triangle is known - a,b,c
Semi perimeter (s) = (a+b+c)/2
Area = square root of (s*(s-a)*(s-b)*(s-c))
"""

a = float(input("Enter first side:"))
b = float(input("Enter second side:"))
c = float(input("Enter third side:"))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle with given sides is", area)
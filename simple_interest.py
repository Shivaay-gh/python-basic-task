"""
Simple Interest = (P * R * T) / 100
P = Principal amount
R = Rate of Interest
T = Time Duration
"""

Principal = float(input("Enter the Principal amount: "))
Rate = float(input("Enter the Rate of Interest: "))
Time = float(input("Enter the Time: "))
si = (Principal * Time * Rate) / 100
print("Simple Interest = ", si)
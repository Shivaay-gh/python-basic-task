"""
Amount = P(1 + R/100) ** T
ci = Amount - P
"""

Principal = float(input("Enter the Principal amount: "))
Rate = float(input("Enter the Rate of Interest: "))
Time = float(input("Enter the Time: "))
# amount1 = Principal * (1+Rate/100) ** Time
amount2 = Principal * pow((1+Rate/100),Time)
print(round(amount2, 2))
ci = amount2 - Principal
print("compound interest", round(ci))




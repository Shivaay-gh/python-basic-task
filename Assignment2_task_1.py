print("Want to know whether your number is Even or Odd!")
try:
   num = int(input("Enter your number: "))

   if num % 2 == 0:
      print("Even")
   else:
      print("Odd")

except ValueError:
    print("Please enter a valid integer.")

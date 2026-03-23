students = {
    "Alice": 85,
    "Rahul": 92,
    "Shubham": 95,
    "Charlie": 90
}

students_lower = {key.lower(): value for key, value in students.items()}

name = input("Enter the student's name: ").strip().lower()

try:
    marks = students_lower[name]
    print(f"{name.capitalize()}'s marks are: {marks}")

except KeyError:
    print("Student record not found.")
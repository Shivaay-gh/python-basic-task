text = input("Enter text to write to the file: ")

with open("Output.txt", "w") as file:
    file.write(text + '\n')

print("Data successfully written to the output.txt")

additional_text = input("Enter additional text to append: ")

with open("Output.txt", "a") as file:
    file.write(additional_text + '\n')

print("Data successfully appended")

print("\nFinal content of output.txt: ")

with open("output.txt", 'r') as file:
    content = file.read()
    print(content)
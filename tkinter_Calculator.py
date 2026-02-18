from tkinter import *


class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.title("Simple Calculator")
        self.window.geometry("350x400")

        self.entry = Entry(window, width=25, borderwidth=5, font=('Arial', 18))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.first_number = None
        self.operator = None


        self.create_buttons()


    def click(self, num):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, current + str(num))


    def set_operator(self, op):
        try:
            self.first_number = float(self.entry.get())
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(0, "ERROR")
            return
        self.operator = op
        self.entry.delete(0, END)


    def equal(self):
        try:
            second_number = float(self.entry.get())
        except ValueError:
            self.entry.delete(0, END)
            self.entry.insert(0, "ERROR")
            return

        self.entry.delete(0, END)
        try:
            if self.operator == "+":
                self.entry.insert(0, self.first_number + second_number)
            elif self.operator == "-":
                self.entry.insert(0, self.first_number - second_number)
            elif self.operator == "*":
                self.entry.insert(0, self.first_number * second_number)
            elif self.operator == "/":
                self.entry.insert(0, self.first_number / second_number)
        except ZeroDivisionError:
            self.entry.insert(0, "ERROR")


    def clear(self):
        self.entry.delete(0, END)
        self.first_number = None
        self.operator = None


    def create_buttons(self):
        # Number buttons
        numbers = [
            (1, 1, 0), (2, 1, 1), (3, 1, 2),
            (4, 2, 0), (5, 2, 1), (6, 2, 2),
            (7, 3, 0), (8, 3, 1), (9, 3, 2),
            (0, 4, 1)
        ]
        for num, row, col in numbers:
            Button(self.window, text=str(num), width=10, height=2,
                   command=lambda n=num: self.click(n)).grid(row=row, column=col, padx=5, pady=5)


        operators = {
            "+": (1, 3), "-": (2, 3), "*": (3, 3), "/": (4, 3)
        }
        for op, (row, col) in operators.items():
            Button(self.window, text=op, width=10, height=2,
                   command=lambda o=op: self.set_operator(o)).grid(row=row, column=col, padx=5, pady=5)


        Button(self.window, text="=", width=10, height=2, command=self.equal).grid(row=4, column=2, padx=5, pady=5)


        Button(self.window, text="Clear", width=10, height=2, command=self.clear).grid(row=4, column=0, padx=5, pady=5)


        Button(self.window, text=".", width=10, height=2, command=lambda: self.click(".")).grid(row=4, column=1, padx=5,
                                                                                                pady=5)


window = Tk()
calc = Calculator(window)
window.mainloop()

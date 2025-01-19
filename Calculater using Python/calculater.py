from tkinter import *
import math  # For sin, cos, tan operations

class Calculator:
    def __init__(self, master):
        master.title("Microsoft Calculator")
        master.geometry("400x700+0+0")  # Increased height for extra row
        master.config(bg="#2d2d2d")  # Dark background for the calculator
        master.resizable(False, False)  # Fixed window size to prevent resizing

        self.equation = StringVar()
        self.entry_value = ""
        self.history = []  # Store calculation history

        # Display area for the equation/result
        self.display = Entry(master, width=25, bg="#3e3e3e", fg="white", font=('Arial', 28), textvariable=self.equation, bd=5, insertwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

        # Button Layout (Microsoft Calculator style)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', '√', '%', '←'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == '=':
                self.create_button(master, button, row_val, col_val, 1, 2, "#4CAF50", self.solve)  # '=' button (Green)
                col_val += 2
            elif button == 'C':
                self.create_button(master, button, row_val, col_val, 1, 1, "#F44336", self.clear)  # Clear button (Red)
                col_val += 1
            elif button == '←':
                self.create_button(master, button, row_val, col_val, 1, 1, "#2196F3", self.backspace)  # Backspace button (Blue)
                col_val += 1
            elif button == '√':
                self.create_button(master, button, row_val, col_val, 1, 1, "#FF9800", self.square_root)  # Square root button (Orange)
                col_val += 1
            elif button == '%':
                self.create_button(master, button, row_val, col_val, 1, 1, "#FF9800", self.reciprocal)  # Reciprocal button (Orange)
                col_val += 1
            else:
                self.create_button(master, button, row_val, col_val, 1, 1, "#505050", lambda b=button: self.show(b))  # Regular buttons (Gray)
                col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

        # Add sin, cos, and tan buttons below the '=' button
        trig_buttons = ['sin', 'cos', 'tan','π']
        for i, trig in enumerate(trig_buttons):
            self.create_button(master, trig, row_val, i, 1, 1, "#009688", lambda b=trig: self.trigonometric(b))  # Trigonometric buttons (Teal)
            
        # Configure grid layout for resizing
        for i in range(7):  # Adjusted for 7 rows
            master.grid_rowconfigure(i, weight=1)  # Ensure each row can expand equally
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)  # Ensure each column can expand equally

    def create_button(self, master, text, row, col, rowspan, colspan, bg_color, command):
        """Helper function to create buttons with styling"""
        Button(master, text=text, relief="flat", bg=bg_color, fg="white", font=('Arial', 18),
               command=command).grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)

    def show(self, value):
        """Display value on the screen"""
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def solve(self):
        """Solve the equation and show result"""
        try:
            result = str(eval(self.entry_value))
            self.equation.set(result)
            self.entry_value = result
            self.history.append(self.entry_value)  # Store the result in history
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

    def clear(self):
        """Clear the display"""
        self.entry_value = ""
        self.equation.set("")

    def backspace(self):
        """Backspace functionality to remove the last character"""
        self.entry_value = self.entry_value[:-1]
        self.equation.set(self.entry_value)

    def square_root(self):
        """Square root functionality"""
        try:
            result = str(eval(f"{self.entry_value}**0.5"))
            self.equation.set(result)
            self.entry_value = result
            self.history.append(self.entry_value)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

    def reciprocal(self):
        """Reciprocal functionality (1/x)"""
        try:
            result = str(eval(f"1/{self.entry_value}"))
            self.equation.set(result)
            self.entry_value = result
            self.history.append(self.entry_value)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

    def trigonometric(self, operation):
        """Handle sin, cos, and tan operations"""
        try:
            value = float(self.entry_value)
            if operation == 'sin':
                result = str(math.sin(math.radians(value)))  # Convert to radians before applying sin
            elif operation == 'cos':
                result = str(math.cos(math.radians(value)))  # Convert to radians before applying cos
            elif operation == 'tan':
                result = str(math.tan(math.radians(value)))  # Convert to radians before applying tan
            self.equation.set(result)
            self.entry_value = result
            self.history.append(self.entry_value)
        except Exception:
            self.equation.set("Error")
            self.entry_value = ""

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()

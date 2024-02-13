from tkinter import *

def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.entry_var = StringVar()
        self.entry_var.set("")

        entry_frame = Frame(master)
        entry_frame.pack(side=TOP, pady=10)

        entry = Entry(entry_frame, textvariable=self.entry_var, font=("Arial", 14), justify="right", bd=5)
        entry.pack(fill=X, expand=True, padx=10)

        button_frame = Frame(master)
        button_frame.pack()

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            button_row = Frame(button_frame)
            button_row.pack(side=TOP)

            for button_text in row:
                button = Button(button_row, text=button_text, width=5, height=2, command=lambda t=button_text: self.button_click(t))
                button.pack(side=LEFT, padx=5, pady=5)

    def button_click(self, button_text):
        current_text = self.entry_var.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            self.entry_var.set(current_text + button_text)

def main():
    root = Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

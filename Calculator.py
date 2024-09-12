import tkinter as tk
from tkinter import dialog_box


def calculate():
    try:
        num1 = entry1.get()
        num2 = entry2.get()
        operation = operation_var.get()

        if not num1.isdigit() or not num2.isdigit():
            dialog_box.showerror("Input Error", "Please enter valid numbers")
            return

        num1 = int(num1)
        num2 = int(num2)

        if operation == '*':
            result = num1 * num2
        elif operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '/':
            if num2 == 0:
                dialog_box.showerror("Math Error", "Division by zero is not allowed")
                return
            result = num1 / num2


        result_label.config(text=f"Result: {result}")
        history_listbox.insert(tk.END, f"{num1} {operation} {num2} = {result}")

    except Exception as e:
        dialog_box.showerror("Error", str(e))


tkinter = tk.Tk()
tkinter.title("Simple Calculator")
tkinter.geometry("400x400")


operation_var = tk.StringVar(value='+')
tk.Label(tkinter, text="Choose operation:").pack()
tk.OptionMenu(tkinter, operation_var, "+", "-", "*", "/").pack()

tk.Label(tkinter, text="Enter the first number:").pack()
entry1 = tk.Entry(tkinter)
entry1.pack()

tk.Label(tkinter, text="Enter the second number:").pack()
entry2 = tk.Entry(tkinter)
entry2.pack()


tk.Button(tkinter, text="Calculate", command=calculate).pack()


result_label = tk.Label(tkinter, text="Result: ")
result_label.pack()


tk.Label(tkinter, text="Operation History:").pack()
history_listbox = tk.Listbox(tkinter)
history_listbox.pack()


tkinter.mainloop()

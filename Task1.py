import tkinter as tk

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2

        elif operation == '-':
            result = num1 - num2

        elif operation == '*':
            result = num1 * num2

        elif operation == '/':
            if num2 == 0:
                result = "Error: Division by zero."
            else:
                result = num1 / num2

        else:
            result = "Error: Invalid operation."

        result_label.config(text=f"The result is: {result}", fg="white", bg="green")

    except ValueError:
        result_label.config(text="Error: Invalid input.", fg="white", bg="red")

num1_entry = tk.Entry(root, bg="white", fg="black")
root = (link unavailable)()
root.title("Calculator")
root.configure(bg="gray")
num1_label = tk.Label(root, text="Enter the first number:", bg="gray", fg="white")
num1_label.pack()
num1_entry.pack()

num2_label = tk.Label(root, text="Enter the second number:", bg="gray", fg="white")
num2_label.pack()
num2_entry = tk.Entry(root, bg="white", fg="black")
num2_entry.pack()

operation_label = tk.Label(root, text="Select an operation:", bg="gray", fg="white")
operation_label.pack()
operation_var = tk.StringVar(root)
operation_var.set("+")
operation_dropdown = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_dropdown.config(bg="white", fg="black")
operation_dropdown.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="blue", fg="white")
calculate_button.pack()

result_label = tk.Label(root, text="", bg="gray", fg="white")
result_label.pack()

root.mainloop()

import tkinter as tk
   

root = tk.Tk()
root.title("ماشین حساب")
window_width = 500
window_height = 300

operation_var = tk.StringVar()  # Define the operation variable


def button_operation(operation):
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        if operation == "+":
            result = num1 + num2
            result_label.config(text="جواب: " + str(result))
        elif operation == "-":
            result = num1 - num2
            result_label.config(text="جواب: " + str(result))
        elif operation == "*":
            result = num1 * num2
            result_label.config(text="جواب: " + str(result))
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                result_label.config(text="جواب: " + str(result))
            else:
                result_label.config(text="نمی توان بر صفر تقسیم کرد!")
        elif operation == "=":
            result_label.config(text="")
    except ValueError:
        result_label.config(text="لطفا اعداد معتبر وارد کنید")


button_sum = tk.Button(root, text="جمع (+)", width=10,
                       height=2, command=lambda: button_operation("+"))
button_subtract = tk.Button(
    root, text="تفریق (-)", width=10, height=2, command=lambda: button_operation("-"))
button_multiply = tk.Button(
    root, text="ضرب (*)", width=10, height=2, command=lambda: button_operation("*"))
button_divide = tk.Button(root, text="تقسیم (/)", width=10,
                          height=2, command=lambda: button_operation("/"))

button_sum.grid(row=3, column=0, padx=5, pady=5)
button_subtract.grid(row=3, column=1, padx=5, pady=5)
button_multiply.grid(row=3, column=2, padx=5, pady=5)
button_divide.grid(row=4, column=1, padx=5, pady=5)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

entry1_label = tk.Label(root, text="عدد اول:")
entry1_label.grid(row=0, column=0, sticky="e")
entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2_label = tk.Label(root, text="عدد دوم:")
entry2_label.grid(row=1, column=0, sticky="e")
entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="جواب:")
result_label.grid(row=2, column=0, columnspan=2)


root.mainloop()

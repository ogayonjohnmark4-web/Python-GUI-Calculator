#1. Importing the Tkinter Library
import tkinter as tk

#2. Creating the Main Window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

#3. Creating a Variable for the Expression
expression = ""

#4. Creating the Calculator Display
display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="brown",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)

#Positioning the Display
display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)

#5. Creating a Function for Keyboard Input Validation
def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"

#6. Synchronizing the Display and Expression Variable
def sync_expression(event):
    global expression
    expression = display.get()

#7. Connecting Keyboard Events Using bind()
display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)

#8. Creating the Button Click Function
def button_click(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

#9. Creating the Clear Function
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

#10. Creating the Calculate Function
def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""

#11. Creating a Two-Dimensional List for the Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

#12. Creating a Frame
button_frame = tk.Frame(
    window,
    bg="#1e1e1e"
)

#Positioning the Frame
button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)

#13. Creating the Clear Button
clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 18, "bold"),
    bg="#ff4444",
    fg="white",
    bd=0,
    command=clear
)

#Positioning the Clear Button
clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)

#14. Generating Buttons Using Nested Loops
for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):
        if value == "=":
            command = calculate
            color = "#00a86b"
        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#ff9500"
        else:
            command = lambda v=value: button_click(v)
            color = "#3a3a3a"



        #15. Creating Each Calculator Button
        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        )

        #16. Positioning the Generated Buttons
        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )

#17. Configuring Grid Rows and Columns
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
 
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

#18. Running the Application
window.mainloop()

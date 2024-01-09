import tkinter as tk
from tkinter import ttk

def on_button_click(value):
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + str(value))

def clear_entry():
    operation_entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(operation_entry.get())
        operation_entry.delete(0, tk.END)
        operation_entry.insert(tk.END, str(result))
    except Exception as e:
        operation_entry.delete(0, tk.END)
        operation_entry.insert(tk.END, "Error")
def divide():
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + "/")
def perform_addition():
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + "+")
def perform_subtraction():
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + "-")
def perform_multiplication():
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + "*")
def perform_delete():
    current_text = operation_entry.get()
    operation_entry.delete(0, tk.END)
    operation_entry.insert(tk.END, current_text + "|")

    
#root window
root = tk.Tk()
root.geometry("300x250")
root.title("Calculator")
root.resizable(0,0)

#configure the grid
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

#display
display_label=tk.Text(root, height=1, width=19, font=("sans-serif",24))
display_label.grid(columnspan=5)

#entries
operation_entry = ttk.Entry(root)
operation_entry.grid(column=0,row=0,sticky=tk.EW, columnspan =4, padx=5,pady=5)

button_7 =tk.Button(root,text="7", command=lambda: on_button_click(7), width=6, font=("sans-serif",14))
button_7.grid(column=0,row=1,sticky=tk.E,padx=5,pady=5)

button_8 =tk.Button(root,text="8", command=lambda: on_button_click(8), width=6, font=("sans-serif",14))
button_8.grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)

button_9 =tk.Button(root,text="9", command=lambda: on_button_click(9), width=6, font=("sans-serif",14))
button_9.grid(column=2,row=1,sticky=tk.E,padx=5,pady=5)

button_div =tk.Button(root,text="/", command=divide, width=6, font=("sans-serif",14))
button_div.grid(column=3,row=1,sticky=tk.E,padx=5,pady=5)

button_4 =tk.Button(root,text="4", command=lambda: on_button_click(4), width=6, font=("sans-serif",14))
button_4.grid(column=0,row=2,sticky=tk.E,padx=5,pady=5)

button_5 =tk.Button(root,text="5", command=lambda: on_button_click(5), width=6, font=("sans-serif",14))
button_5.grid(column=1,row=2,sticky=tk.E,padx=5,pady=5)

button_6 =tk.Button(root,text="6", command=lambda: on_button_click(6), width=6, font=("sans-serif",14))
button_6.grid(column=2,row=2,sticky=tk.E,padx=5,pady=5)

button_mult =tk.Button(root,text="*", command=perform_multiplication, width=6, font=("sans-serif",14))
button_mult.grid(column=3,row=2,sticky=tk.E,padx=5,pady=5)

button_C =tk.Button(root,text="C", command=clear_entry, width=6, font=("sans-serif",14))
button_C.grid(column=1,row=4,sticky=tk.E,padx=5,pady=5)
              
button_CE =tk.Button(root,text="CE", command=clear_entry, width=6, font=("sans-serif",14))
button_CE.grid(column=2,row=4,sticky=tk.E,padx=5,pady=5)

button_0 =tk.Button(root,text="0", command=lambda: on_button_click(0), width=6, font=("sans-serif",14))
button_0.grid(column=0,row=4,sticky=tk.E,padx=5,pady=5)

button_1 =tk.Button(root,text="1", command=lambda: on_button_click(1), width=6, font=("sans-serif",14))
button_1.grid(column=0,row=3,sticky=tk.E,padx=5,pady=5)

button_2 =tk.Button(root,text="2", command=lambda: on_button_click(2), width=6, font=("sans-serif",14))
button_2.grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)

button_3=tk.Button(root,text="3", command=lambda: on_button_click(3), width=6, font=("sans-serif",14))
button_3.grid(column=2,row=3,sticky=tk.E,padx=5,pady=5)

button_add =tk.Button(root,text="+", command=perform_addition, width=6, font=("sans-serif",14))
button_add.grid(column=3,row=3,sticky=tk.E,padx=5,pady=5)

button_equal =tk.Button(root,text="=", command=calculate_result, width=6, font=("sans-serif",14))
button_equal.grid(column=3,row=4,sticky=tk.E,padx=5,pady=5)

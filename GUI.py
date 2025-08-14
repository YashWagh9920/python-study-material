import tkinter as tk

root = tk.Tk()
root.title("YASH WAGH 122A1125")
root.geometry("800x600")
root.configure(bg="blue")

label = tk.Label(root, text="Hello Yash SIES", font=("Consolas", 40), bg="lightgrey", fg="black")
label.pack(pady=20)

def button_click():
    print('Button clicked')

button = tk.Button(root, text="Click Me", command=button_click, padx=10, pady=5,
                   bg="brown", fg="black", font=("Arial", 16))
button.pack(pady=10)

def checkbutton_clicked():
    if var.get() == 0:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")

var = tk.IntVar()

checkbutton1 = tk.Checkbutton(root, text="Check Button 1", variable=var, command=checkbutton_clicked, bg="red", fg="black")
checkbutton1.pack(pady=10)

checkbutton2 = tk.Checkbutton(root, text="Check Button 2", variable=var, command=checkbutton_clicked, bg="red", fg="black")
checkbutton2.pack()

def on_select(event):
    selected_items = [listbox.get(idx) for idx in listbox.curselection()]
    print("Selected items:", selected_items)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, bg="pink", fg="black",
                     selectbackground="yellow", selectforeground="white", font=("Arial", 12))
listbox.pack(pady=20, padx=50)

for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

listbox.bind("<<ListboxSelect>>", on_select)

def radio_button_selected():
    selected_option = var.get()
    if selected_option == 1:
        print("Option 1 selected")
    elif selected_option == 2:
        print("Option 2 selected")
    elif selected_option == 3:
        print("Option 3 selected")

var = tk.IntVar()

option1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1,
                          command=radio_button_selected, bg="yellow", fg="black")
option1.pack(pady=5)

option2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2,
                          command=radio_button_selected, bg="yellow", fg="black")
option2.pack(pady=5)

option3 = tk.Radiobutton(root, text="Option 3", variable=var, value=3,
                          command=radio_button_selected, bg="yellow", fg="black")
option3.pack(pady=5)

def get_entry_text():
    text = entry.get()
    print("Entry Text:", text)

entry = tk.Entry(root, font=("Arial", 14), bg="yellow", fg="black")
entry.pack(pady=10)

button = tk.Button(root, text="Get Entry Text", command=get_entry_text, bg="yellow", fg="black", font=("Arial", 14))
button.pack(pady=5)

def get_text():
    text = text_widget.get(1.0, tk.END)
    print("Text:", text)

text_widget = tk.Text(root, height=10, width=40, font=("Arial", 12), bg="yellow", fg="black")
text_widget.pack(pady=10)
initial_text = "This is a Text Widget.\nYou can enter and edit text here."
text_widget.insert(tk.END, initial_text)
button= tk.Button(root, text="Get Text", command=get_text, bg="yellow", fg="black", font=("Arial", 14))
button.pack(pady=5)
root.mainloop()

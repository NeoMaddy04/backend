import tkinter as tk
from tkinter import messagebox, ttk

def submit_form():
    # Check if the "File ID" entry is empty
    if not file_id_entry.get().strip():
        messagebox.showerror("Error", "File ID is mandatory.")
        return  # Exit the function if File ID is empty

    # Check if any other field is empty based on the selected option
    if selected_option.get() == "Modal":
        if not all((scale_var.get(), gap_var.get(), thickness_var.get(), proportions_var.get(), details_var.get())):
            messagebox.showerror("Error", "All fields are mandatory.")
            return
    elif selected_option.get() == "Texture":
        if not all((pivot_var.get(), metalness_var.get(), details_var.get())):
            messagebox.showerror("Error", "All fields are mandatory.")
            return

    # Show the form submission message
    messagebox.showinfo("Form Submitted")

    # Refresh the form
    refresh_form()

def refresh_form():
    # Clear all widgets
    for widget in app.winfo_children():
        widget.destroy()
    
    # Recreate the form widgets
    create_form_widgets()

def create_form_widgets():
    # Label for selecting option
    option_label = tk.Label(app, text="Select an option:", font=("Arial", 12))
    option_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    global selected_option
    selected_option = tk.StringVar()
    combobox = ttk.Combobox(app, textvariable=selected_option, values=["Modal", "Texture"], font=("Arial", 12))
    combobox.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

    # Function to handle the selection change
    def on_selection_change(*args):
        # Clear all widgets except the combobox
        for widget in app.winfo_children():
            if widget!= combobox:
                widget.destroy()
        
        option_label = tk.Label(app, text="Select an option:", font=("Arial", 12))
        option_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        # Recreate the form widgets based on the selected option
        if selected_option.get() == "Modal":
            create_modal_options()
        elif selected_option.get() == "Texture":
            create_texture_options()

    # Bind the selection change event to the function
    combobox.bind("<<ComboboxSelected>>", on_selection_change)

    # Initial form creation based on the selected option
    if selected_option.get() == "Modal":
        create_modal_options()
    elif selected_option.get() == "Texture":
        create_texture_options()

# Function to create form options for Modal
def create_modal_options():
    global file_id_entry, scale_var, gap_var, thickness_var, proportions_var, details_var

    file_id_label = tk.Label(app, text="File ID:", font=("Arial", 12))
    file_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    file_id_entry = tk.Entry(app, font=("Arial", 12))
    file_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    scale_var = tk.BooleanVar()
    scale_check = tk.Checkbutton(app, text="Scale", bg="white", fg="black", variable=scale_var, font=("Arial", 12))
    scale_check.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    gap_var = tk.BooleanVar()
    gap_check = tk.Checkbutton(app, text="Gap", bg="white", fg="black", variable=gap_var, font=("Arial", 12))
    gap_check.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    thickness_var = tk.BooleanVar()
    thickness_check = tk.Checkbutton(app, text="Thickness", bg="white", fg="black", variable=thickness_var, font=("Arial", 12))
    thickness_check.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    proportions_var = tk.BooleanVar()
    proportions_check = tk.Checkbutton(app, text="Proportions", bg="white", fg="black", variable=proportions_var, font=("Arial", 12))
    proportions_check.grid(row=7, column=1, padx=10, pady=10, sticky="w")

    details_var = tk.BooleanVar()
    details_check = tk.Checkbutton(app, text="Details", bg="white", fg="black", variable=details_var, font=("Arial", 12))
    details_check.grid(row=8, column=0, padx=10, pady=10, sticky="w")

    submit_button = tk.Button(app, text="Submit", command=submit_form, font=("Arial", 12))
    submit_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Function to create form options for Texture
def create_texture_options():
    global file_id_entry, pivot_var, metalness_var, details_var

    file_id_label = tk.Label(app, text="File ID:", font=("Arial", 12))
    file_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    file_id_entry = tk.Entry(app, font=("Arial", 12))
    file_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    pivot_var = tk.BooleanVar()
    pivot_check = tk.Checkbutton(app, text="Pivot", bg="white", fg="black", variable=pivot_var, font=("Arial", 12))
    pivot_check.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    metalness_var = tk.BooleanVar()
    metalness_check = tk.Checkbutton(app, text="Metalness (Texture issues)", bg="white", fg="black", variable=metalness_var, font=("Arial", 12))
    metalness_check.grid(row=6, column=1, padx=10, pady=10, sticky="w")

    details_var = tk.BooleanVar()
    details_check = tk.Checkbutton(app, text="Details (logos, patterns, stickers)", bg="white", fg="black", variable=details_var, font=("Arial", 12))
    details_check.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    submit_button = tk.Button(app, text="Submit", command=submit_form, font=("Arial", 12))
    submit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

app = tk.Tk()
app.title("QC Check List")
app.config(bg="white")

create_form_widgets()

# Run the application
app.mainloop()

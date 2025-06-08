import tkinter as tk
from tkinter import ttk, messagebox
from validation.validator_liliwelt import Validator

def show_register(container):
    """
    Display the user registration form inside the given container.
    """
    clear(container)  # Remove any previous content from the container

    # Create a frame to hold the registration form
    frame = ttk.Frame(container)
    frame.pack(fill='both', expand=True, padx=20, pady=20)

    # Title for the form
    ttk.Label(frame, text="Register", font=("Helvetica", 16)).pack(pady=10)

    # Dictionary to hold user input values using StringVar()
    fields = {
        "Name": tk.StringVar(),
        "Address": tk.StringVar(),
        "Postcode": tk.StringVar(),
        "Locality": tk.StringVar(),
        "Email": tk.StringVar(),
        "Phone": tk.StringVar(),
        "Password": tk.StringVar()
    }

    # Create a labeled entry widget for each field
    entries = {}
    for label, var in fields.items():
        ttk.Label(frame, text=label).pack()
        show = '*' if label == "Password" else None  # Hide password input
        entry = ttk.Entry(frame, textvariable=var, show=show)
        entry.pack()
        entries[label] = entry  # Store the entry widget if needed later

    # Function called when "Submit" is pressed
    def submit():

        # Collect user input from all form fields into a dictionary
        data = {label: var.get() for label, var in fields.items()}

        # Validate each field using your Validator class

        try:

            if not Validator.validate_name(data["Name"]):
                raise ValueError("Invalid name.")

            if not Validator.validate_address(data["Address"]):
                raise ValueError("Invalid address.")

            if not Validator.validate_postcode(data["Postcode"]):
                raise ValueError("Invalid postcode.")

            if not Validator.validate_locality(data["Locality"]):
                raise ValueError("Invalid locality.")

            if not Validator.validate_email(data["Email"]):
                raise ValueError("Invalid email.")

            if not Validator.validate_phone(data["Phone"]):
                raise ValueError("Invalid phone.")

            if not Validator.validate_password(data["Password"]):
                raise ValueError("Invalid password.")

            # If all validations pass, show success (DB saving could go here)

            print("New registration:", data)

            messagebox.showinfo("Success", "User registered successfully!")

        except ValueError as e:

            messagebox.showerror("Validation Error", str(e))

    # Submit button
    ttk.Button(frame, text="Submit", command=submit).pack(pady=10)

def clear(container):
    """
    Remove all widgets from the container (used before showing a new view).
    """
    for widget in container.winfo_children():
        widget.destroy()


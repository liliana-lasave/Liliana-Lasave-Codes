import tkinter as tk
from tkinter import ttk, messagebox

def show_login(container):
    """
    Display the login form inside the given container.
    """
    clear(container)  # Remove previous content from the container

    # Create a new frame to hold the login form
    frame = ttk.Frame(container)
    frame.pack(fill='both', expand=True, padx=20, pady=20)

    # Form title
    ttk.Label(frame, text="Login", font=("Helvetica", 16)).pack(pady=10)

    # Email input
    ttk.Label(frame, text="Email").pack()
    email_entry = ttk.Entry(frame)
    email_entry.pack()

    # Password input (with hidden characters)
    ttk.Label(frame, text="Password").pack()
    pass_entry = ttk.Entry(frame, show='*')
    pass_entry.pack()

    # Login button
    ttk.Button(
        frame,
        text="Login",
        command=lambda: attempt_login(email_entry.get(), pass_entry.get())
    ).pack(pady=10)

def attempt_login(email, password):
    """
    Placeholder for login logic. You can connect this to your Customer data.
    """
    print(f"Trying to log in with email: {email}, password: {password}")

    # TODO: Check credentials against your data
    messagebox.showinfo("Login", f"Login attempted for: {email}")

def clear(container):
    """
    Remove all widgets from the container (used before loading a new view).
    """
    for widget in container.winfo_children():
        widget.destroy()


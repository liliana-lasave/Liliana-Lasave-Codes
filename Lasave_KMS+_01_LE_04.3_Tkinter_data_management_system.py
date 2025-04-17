import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, date
import re

# File path (update if needed)
file_path = "user_register.txt"


# ---------------------- VALIDATION FUNCTIONS ----------------------
def clean_input(text):
    return ' '.join(text.strip().split())


def validate_name(name):
    pattern = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÄËÏÖÜäëïöü]+(?:[-'][A-Za-zÁÉÍÓÚáéíóúÑñÄËÏÖÜäëïöü]+)?$")
    parts = name.split()
    return len(parts) == 2 and all(pattern.match(part) for part in parts)


def validate_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None


def validate_birthdate(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email) is not None and len(email) <= 254


# ---------------------- FILE HANDLING ----------------------
def read_users():
    try:
        with open(file_path, "r") as file:
            return [line.strip().split(',') for line in file]
    except FileNotFoundError:
        return []


def save_user(data):
    with open(file_path, "a") as file:
        file.write(','.join(data) + "\n")


def update_users(users):
    with open(file_path, "w") as file:
        for user in users:
            file.write(','.join(user) + "\n")


# ---------------------- GUI FUNCTIONS ----------------------
def register_user():
    def submit():
        data = [
            name_entry.get(),
            phone_entry.get(),
            birth_entry.get(),
            street_entry.get(),
            town_entry.get(),
            email_entry.get()
        ]

        # Validate all fields
        if not validate_name(data[0]):
            messagebox.showerror("Error", "Invalid name format (First Last)")
            return
        if not validate_phone(data[1]):
            messagebox.showerror("Error", "Phone must be 10 digits")
            return
        if not validate_birthdate(data[2]):
            messagebox.showerror("Error", "Birthdate must be dd/mm/yyyy")
            return
        if not data[3]:
            messagebox.showerror("Error", "Street address required")
            return
        if not data[4]:
            messagebox.showerror("Error", "Town required")
            return
        if not validate_email(data[5]):
            messagebox.showerror("Error", "Invalid email")
            return

        save_user(data)
        messagebox.showinfo("Success", "User registered successfully!")
        register_win.destroy()

    register_win = tk.Toplevel()
    register_win.title("Register User")

    tk.Label(register_win, text="Name (First Last):").grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(register_win)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(register_win, text="Phone (10 digits):").grid(row=1, column=0, padx=5, pady=5)
    phone_entry = tk.Entry(register_win)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(register_win, text="Birthdate (dd/mm/yyyy):").grid(row=2, column=0, padx=5, pady=5)
    birth_entry = tk.Entry(register_win)
    birth_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(register_win, text="Street Address:").grid(row=3, column=0, padx=5, pady=5)
    street_entry = tk.Entry(register_win)
    street_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(register_win, text="Town and Postcode:").grid(row=4, column=0, padx=5, pady=5)
    town_entry = tk.Entry(register_win)
    town_entry.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(register_win, text="Email:").grid(row=5, column=0, padx=5, pady=5)
    email_entry = tk.Entry(register_win)
    email_entry.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(register_win, text="Submit", command=submit).grid(row=6, columnspan=2, pady=10)


def search_users():
    def perform_search():
        search_term = entry.get().lower()
        criteria = var.get()
        results.delete(0, tk.END)

        users = read_users()
        current_month = datetime.now().strftime("%m")

        for user in users:
            if criteria == "name" and search_term in user[0].lower():
                results.insert(tk.END, user[0])
            elif criteria == "birth_month" and user[2].split('/')[1] == search_term.zfill(2):
                results.insert(tk.END, user[0])
            elif criteria == "town" and search_term in user[4].lower():
                results.insert(tk.END, user[0])
            elif criteria == "current_month" and user[2].split('/')[1] == current_month:
                results.insert(tk.END, user[0])

    search_win = tk.Toplevel()
    search_win.title("Search Users")

    var = tk.StringVar(value="name")
    ttk.Radiobutton(search_win, text="Name", variable=var, value="name").pack(anchor='w')
    ttk.Radiobutton(search_win, text="Birth Month (mm)", variable=var, value="birth_month").pack(anchor='w')
    ttk.Radiobutton(search_win, text="Town", variable=var, value="town").pack(anchor='w')
    ttk.Radiobutton(search_win, text="This Month's Birthdays", variable=var, value="current_month").pack(anchor='w')

    entry = tk.Entry(search_win)
    entry.pack(pady=5)

    tk.Button(search_win, text="Search", command=perform_search).pack()
    results = tk.Listbox(search_win, width=50)
    results.pack(pady=10)


def modify_user():
    name = simpledialog.askstring("Modify User", "Enter name to modify:")
    if not name:
        return

    users = read_users()
    found = None
    for user in users:
        if name.lower() in user[0].lower():
            found = user
            break

    if not found:
        messagebox.showerror("Error", "User not found")
        return

    def save_changes():
        new_data = [
            name_entry.get(),
            phone_entry.get(),
            birth_entry.get(),
            street_entry.get(),
            town_entry.get(),
            email_entry.get()
        ]
        users.remove(found)
        users.append(new_data)
        update_users(users)
        messagebox.showinfo("Success", "User updated!")
        modify_win.destroy()

    modify_win = tk.Toplevel()
    modify_win.title("Edit User")

    tk.Label(modify_win, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(modify_win)
    name_entry.insert(0, found[0])
    name_entry.grid(row=0, column=1)

    tk.Label(modify_win, text="Phone:").grid(row=1, column=0)
    phone_entry = tk.Entry(modify_win)
    phone_entry.insert(0, found[1])
    phone_entry.grid(row=1, column=1)

    tk.Label(modify_win, text="Birthdate:").grid(row=2, column=0)
    birth_entry = tk.Entry(modify_win)
    birth_entry.insert(0, found[2])
    birth_entry.grid(row=2, column=1)

    tk.Label(modify_win, text="Street:").grid(row=3, column=0)
    street_entry = tk.Entry(modify_win)
    street_entry.insert(0, found[3])
    street_entry.grid(row=3, column=1)

    tk.Label(modify_win, text="Town:").grid(row=4, column=0)
    town_entry = tk.Entry(modify_win)
    town_entry.insert(0, found[4])
    town_entry.grid(row=4, column=1)

    tk.Label(modify_win, text="Email:").grid(row=5, column=0)
    email_entry = tk.Entry(modify_win)
    email_entry.insert(0, found[5])
    email_entry.grid(row=5, column=1)

    tk.Button(modify_win, text="Save", command=save_changes).grid(row=6, columnspan=2, pady=10)


def calculate_birthday():
    date_str = simpledialog.askstring("Birthday Calculator", "Enter birthdate (dd/mm/yyyy):")
    if not date_str:
        return

    try:
        birth_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format")
        return

    today = date.today()
    next_birthday = birth_date.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    days_until = (next_birthday - today).days
    messagebox.showinfo("Result", f"Days until next birthday: {days_until}")


# ---------------------- MAIN WINDOW ----------------------
root = tk.Tk()
root.title("User Management System")
root.geometry("400x300")

tk.Label(root, text="User Management System", font=('Arial', 16)).pack(pady=10)

tk.Button(root, text="Register New User", command=register_user, width=20).pack(pady=5)
tk.Button(root, text="Search Users", command=search_users, width=20).pack(pady=5)
tk.Button(root, text="Modify User", command=modify_user, width=20).pack(pady=5)
tk.Button(root, text="Calculate Birthday", command=calculate_birthday, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)

root.mainloop()
import tkinter as tk
import tkinter.font as tkfont
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

#  return a list of the maximum length of each field to format the printed data neatly.  this will take
#  all the user data strings and return a list of field lengths for each field

def get_field_lengths (user_list):

    max_field_lengths = [0, 0, 0, 0, 0, 0]

    for user in user_list:
        # Split the string by comma

        # Update the max length for each field
        for i in range(6):
            field_length = len(user[i])
            if field_length > max_field_lengths[i]:
                max_field_lengths[i] = field_length

    return max_field_lengths

def get_formatted_user (user, max_field_lengths):

    for i in range (len(user)):
        user[i] = user[i].ljust(max_field_lengths[i])

    formatted_field = "  ".join (user)

    return formatted_field

def search_users():
    def perform_search():
        search_term = entry.get().lower().strip()
        criteria = criteria_button.get()
        results.delete(0, tk.END)

        if search_term == '' and criteria in ["name", "birth_month", "town"]:
            messagebox.showerror("Error", "Fill in the search box for a proper search")
            return

        users = read_users()
        current_month = datetime.now().strftime("%m")
        max_field_lengths = get_field_lengths(users)

        for user in users:
            if criteria == "name" and search_term in user[0].lower():
                print_string = get_formatted_user(user, max_field_lengths)  # format user data for printing
                results.insert(tk.END, print_string)
            elif criteria == "birth_month" and user[2].split('/')[1] == search_term.zfill(2):
                print_string = get_formatted_user(user, max_field_lengths)
                results.insert(tk.END, print_string)
            elif criteria == "town" and search_term in user[4].lower():
                print_string = get_formatted_user(user, max_field_lengths)
                results.insert(tk.END, print_string)
            elif criteria == "current_month" and user[2].split('/')[1] == current_month:
                print_string = get_formatted_user (user, max_field_lengths)
                birthday_string = get_birthday_string (user[2])
                print_string = print_string + "  " + birthday_string
                results.insert(tk.END, print_string)
            elif criteria == "all_users":
                print_string = get_formatted_user(user, max_field_lengths)
                results.insert(tk.END, print_string)

    search_win = tk.Toplevel()
    search_win.title("Search Users")

    criteria_button = tk.StringVar(value="name")
    ttk.Radiobutton(search_win, text="Name", variable=criteria_button, value="name").pack(anchor='w')
    ttk.Radiobutton(search_win, text="Birth Month (mm)", variable=criteria_button, value="birth_month").pack(anchor='w')
    ttk.Radiobutton(search_win, text="Town", variable=criteria_button, value="town").pack(anchor='w')
    ttk.Radiobutton(search_win, text="This Month's Birthdays", variable=criteria_button, value="current_month").pack(anchor='w')
    ttk.Radiobutton(search_win, text="Show All Users", variable=criteria_button, value="all_users").pack(anchor='w')

    entry = tk.Entry(search_win)
    entry.pack(pady=15,anchor='w')

    tk.Button(search_win, text="Search", command=perform_search).pack(anchor='w')
    results = tk.Listbox(search_win, width=150,font="TkFixedFont")
    results.pack(pady=15,anchor='w')

def get_birthday_string (birthday_data):

    current_day = datetime.now().day

    birthday_list = birthday_data.split("/")
    birthday = int (birthday_list[0])

    day_diff = current_day - birthday

    if day_diff > 0:
        birthday_string = f"        They had a birthday {day_diff} day(s) ago"
    elif day_diff < 0:
        day_diff = abs(day_diff)
        birthday_string = f"        They have a birthday in {day_diff} day(s)"
    else:
        birthday_string = f"        Today is their birthday"

    return birthday_string

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





# ---------------------- MAIN WINDOW ----------------------
root = tk.Tk()
root.title("User Management System")
root.geometry("400x300")

tk.Label(root, text="User Management System", font=('Arial', 16)).pack(pady=10)

tk.Button(root, text="Register New User", command=register_user, width=20).pack(pady=5)
tk.Button(root, text="Search Users", command=search_users, width=20).pack(pady=5)
tk.Button(root, text="Modify User", command=modify_user, width=20).pack(pady=5)
tk.Button(root, text="Exit", command=root.destroy, width=20).pack(pady=10)

root.mainloop()
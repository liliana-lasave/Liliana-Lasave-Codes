
import tkinter as tk
from tkinter import ttk, messagebox

def show_login(container, app):
    win = tk.Toplevel(container)
    win.title("Login")

    ttk.Label(win, text="Username").pack()
    euser = ttk.Entry(win); euser.pack(fill='x')

    ttk.Label(win, text="Password").pack()
    epw = ttk.Entry(win, show='•'); epw.pack(fill='x')

    def do_login():
        res = app.storage.authenticate(euser.get(), epw.get())
        if res:
            app.current_user = {
                "id": res[0],
                "is_company": bool(res[1]),
                "company_id": res[2],
                "username": euser.get().strip()
            }
            app.enable_logout()
            messagebox.showinfo("Welcome", f"Logged in as {euser.get()}")
            win.destroy()
        else:
            messagebox.showerror("Fail", "Wrong username or password")

    ttk.Button(win, text="Login", command=do_login).pack(pady=10)

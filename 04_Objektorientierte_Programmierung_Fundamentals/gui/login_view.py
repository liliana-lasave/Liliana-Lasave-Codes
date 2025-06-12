import tkinter as tk

from tkinter import ttk, messagebox


def show_login(container, app):
    """

    Abre una ventana de diálogo para que el usuario

    introduzca username y password y, si son correctos,

    guarda la sesión en app.current_user.

    """

    win = tk.Toplevel(container)

    win.title("Login")

    win.resizable(False, False)

    ttk.Label(win, text="Username").pack(pady=(10, 0))

    entry_user = ttk.Entry(win)

    entry_user.pack(fill="x", padx=10)

    ttk.Label(win, text="Password").pack(pady=(10, 0))

    entry_pw = ttk.Entry(win, show="•")

    entry_pw.pack(fill="x", padx=10)

    def do_login():

        result = app.storage.authenticate(entry_user.get(), entry_pw.get())

        if result:

            app.current_user = {

                "id": result[0],

                "is_company": bool(result[1]),

                "company_id": result[2],

                "username": entry_user.get().strip()

            }

            app.enable_logout()  # habilita la opción Logout en el menú

            messagebox.showinfo(

                "Welcome",

                f"Logged in as {app.current_user['username']}"

            )

            win.destroy()

        else:

            messagebox.showerror("Fail", "Wrong username or password")

    ttk.Button(win, text="Login", command=do_login).pack(pady=15)


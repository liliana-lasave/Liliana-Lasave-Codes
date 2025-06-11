
import tkinter as tk
from tkinter import ttk, messagebox
from validation.validator_liliwelt import Validator as V
from errors.custom_exceptions import SaveError

def show_register(container, storage):
    win = tk.Toplevel(container)
    win.title("Register")

    def row(label):
        frm = ttk.Frame(win); frm.pack(fill='x', pady=2)
        ttk.Label(frm, text=label, width=18, anchor='w').pack(side='left')
        ent = ttk.Entry(frm); ent.pack(side='left', fill='x', expand=True)
        return ent

    e_username = row("Username")
    e_password = row("Password"); e_password.config(show='•')
    e_address  = row("Address")
    e_postcode = row("Postcode")
    e_locality = row("Locality")
    e_email    = row("Email")
    e_phone    = row("Phone")

    is_company = tk.BooleanVar()
    ttk.Checkbutton(win, text="I am a company", variable=is_company).pack(anchor='w')

    e_company  = row("Company number")
    e_birth    = row("Birthdate (DD.MM.YYYY)")

    def toggle():
        if is_company.get():
            e_company.master.pack(fill='x', pady=2)
            e_birth.master.forget()
        else:
            e_birth.master.pack(fill='x', pady=2)
            e_company.master.forget()
    is_company.trace_add('write', lambda *_: toggle())
    toggle()

    def invalid(msg):
        messagebox.showerror("Invalid", msg); return False

    def validate():
        if not V.validate_name(e_username.get()): return invalid("Invalid username")
        if not V.validate_password(e_password.get()): return invalid("Weak password")
        if not V.validate_address(e_address.get()): return invalid("Invalid address")
        if not V.validate_postcode(e_postcode.get()): return invalid("Invalid postcode")
        if not V.validate_locality(e_locality.get()): return invalid("Invalid locality")
        if not V.validate_email(e_email.get()): return invalid("Invalid email")
        if not V.validate_phone(e_phone.get()): return invalid("Invalid phone")
        if is_company.get():
            if not V.validate_company_number(e_company.get()): return invalid("Invalid company number")
        else:
            if not V.validate_birthdate(e_birth.get()): return invalid("Invalid birthdate")
        return True

    def do_register():
        if not validate(): return
        try:
            storage.register_user(
                username=e_username.get(),
                password=e_password.get(),
                address=e_address.get(),
                postcode=e_postcode.get(),
                locality=e_locality.get(),
                email=e_email.get(),
                phone=e_phone.get(),
                is_company=is_company.get(),
                company_number=e_company.get() if is_company.get() else None,
                birthdate=e_birth.get() if not is_company.get() else None
            )
            messagebox.showinfo("Success", "Registration complete – please log in.")
            win.destroy()
        except SaveError as e:
            messagebox.showerror("Error", str(e))

    ttk.Button(win, text="Register", command=do_register).pack(pady=10)

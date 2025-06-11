
import sys, os, tkinter as tk
from tkinter import ttk, messagebox
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from products.storage_liliwelt import Storage
from catalogue_frame import CatalogueFrame
from cart_frame import CartFrame
from checkout_frame import CheckoutFrame
from payment_frame import PaymentFrame
from thankyou_frame import ThankYouFrame
from login_view import show_login
from register_view import show_register

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('LiliWelt Online Shop')
        self.geometry('800x600')
        db = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'liliwelt.db'))
        self.storage = Storage(db)
        self.storage.create_tables()
        self.cart = self.storage.load_cart()
        self.current_user = None
        self._build_menu()
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)
        self.show_frame(CatalogueFrame)

    # ---- navigation ----
    def show_frame(self, frame_cls, **kwargs):
        for w in self.container.winfo_children():
            w.destroy()
        frame_cls(self.container, self, **kwargs).pack(fill='both', expand=True)

    # ---- menu ----
    def _build_menu(self):
        m = tk.Menu(self); self.config(menu=m)
        self.user_menu = tk.Menu(m, tearoff=0)
        self.user_menu.add_command(label='Login', command=lambda: show_login(self.container, self))
        self.user_menu.add_command(label='Register', command=lambda: show_register(self.container, self.storage))
        self.user_menu.add_command(label='Logout', command=self.logout, state='disabled')
        m.add_cascade(label='User', menu=self.user_menu)
        m.add_command(label='Products', command=lambda: self.show_frame(CatalogueFrame))
        m.add_command(label='Cart', command=lambda: self._need_login() and self.show_frame(CartFrame))
        m.add_command(label='Checkout', command=lambda: self._need_login() and self.show_frame(CheckoutFrame))

    def enable_logout(self):
        self.user_menu.entryconfigure('Logout', state='normal')

    def logout(self):
        if messagebox.askyesno('Logout', 'Do you really want to log out?'):
            self.current_user = None
            self.user_menu.entryconfigure('Logout', state='disabled')
            messagebox.showinfo('Logged out', 'Session closed.')

    def _need_login(self):
        if self.current_user:
            return True
        messagebox.showwarning('Login required', 'Please log in first.')
        return False

if __name__ == '__main__':
    App().mainloop()

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import tkinter as tk
from tkinter import ttk
from order_view import show_order

# Create tables before starting
from products.storage_liliwelt import Storage
Storage("liliwelt.db").create_tables()

# Importing views for different sections of the app
from login_view import show_login
from register_view import show_register
from product_view import ProductView
from cart_view import open_cart_view

class LiliWeltApp(tk.Tk):
    """
    Main application window for the LiliWelt Online Shop.
    This initializes the main layout, menu, and default view.
    """

    def __init__(self):
        super().__init__()

        # Set window title and dimensions
        self.title("LiliWelt Online Shop")
        self.geometry("800x600")

        # Shared cart
        self.cart = []

        # Create the top menu bar
        self.create_menu()

        # Frame where different views will be loaded
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        # Load the product view by default
        self.show_products()

    def create_menu(self):
        """Create the top navigation menu with user, product, and order options."""
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # User section: login and registration
        user_menu = tk.Menu(menubar, tearoff=0)
        user_menu.add_command(label="Login", command=lambda: show_login(self.container))
        user_menu.add_command(label="Register", command=lambda: show_register(self.container))
        menubar.add_cascade(label="User", menu=user_menu)

        # Navigation options
        menubar.add_command(label="Products", command=self.show_products)
        menubar.add_command(label="Cart", command=open_cart_view)
        menubar.add_command(label="Checkout", command=lambda: show_order(self.container))

    def show_products(self):
        """Display the product view."""
        for widget in self.container.winfo_children():
            widget.destroy()
        ProductView(self.container, self.cart).pack(fill="both", expand=True)

# Entry point to start the application
if __name__ == "__main__":
    app = LiliWeltApp()
    app.mainloop()

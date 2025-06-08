import tkinter as tk
from tkinter import ttk
from order_view import show_order

# Importing views for different sections of the app
from login_view import show_login
from register_view import show_register
from product_view import show_products
from cart_view import show_cart
from order_view import show_order

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

        # Create the top menu bar
        self.create_menu()

        # Frame where different views will be loaded
        self.container = ttk.Frame(self)
        self.container.pack(fill='both', expand=True)

        # Load the product view by default
        show_products(self.container)

    def create_menu(self):
        """
        Create the top navigation menu with user, product, and order options.
        """

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # User section: login and registration
        user_menu = tk.Menu(menubar, tearoff=0)
        user_menu.add_command(label="Login", command=lambda: show_login(self.container))
        user_menu.add_command(label="Register", command=lambda: show_register(self.container))
        menubar.add_cascade(label="User", menu=user_menu)

        # Navigation options
        menubar.add_command(label="Products", command=lambda: show_products(self.container))
        menubar.add_command(label="Cart", command=lambda: show_cart(self.container))
        menubar.add_command(label="Checkout", command=lambda: show_order(self.container))


# Entry point to start the application
if __name__ == "__main__":
    app = LiliWeltApp()
    app.mainloop()


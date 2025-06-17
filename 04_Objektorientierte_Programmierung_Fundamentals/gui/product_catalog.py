

import tkinter as tk
from tkinter import messagebox, ttk
from database.products_db import get_all_products
from orders.shopping_cart import ShoppingCart


class CatalogueFrame(tk.Frame):
    """
    A frame that displays the product catalogue in a scrollable list.
    Allows users to add products to the shopping cart.
    """

    def __init__(self, master, cart: ShoppingCart, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.cart = cart
        self.products = []

        # Title label
        tk.Label(self, text="Product Catalogue", font=("Arial", 14)).pack(pady=10)

        # Create a scrollable treeview widget to show product list
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Price"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")

        # Attach scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Button to add selected product to cart
        tk.Button(self, text="Add to Cart", command=self.add_to_cart).pack(pady=10)

        # Load product list from database
        self.load_products()

    def load_products(self):
        """Load products from the database and display them in the treeview."""
        try:
            self.products = get_all_products()
            for product in self.products:
                self.tree.insert("", "end", values=(product.id, product.name, f"${product.price:.2f}"))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load products: {e}")

    def add_to_cart(self):
        """Add the selected product to the shopping cart."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a product to add.")
            return

        product_values = self.tree.item(selected_item, 'values')
        product_id = int(product_values[0])

        try:
            self.cart.add_product_by_id(product_id)
            messagebox.showinfo("Added", f"Product ID {product_id} added to cart.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add product to cart: {e}")

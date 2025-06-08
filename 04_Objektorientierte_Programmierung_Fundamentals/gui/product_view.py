
import tkinter as tk
from tkinter import ttk
from products.storage_liliwelt import Storage
from gui.cart_view import open_cart_view
import os

class ProductView(tk.Frame):
    def __init__(self, master, cart, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.cart = cart

        # Debug: Show database path
        db_path = os.path.abspath("../liliwelt.db")
        print("Using database at:", db_path)

        # Load all product objects using Storage
        self.products = Storage(db_path).load_all_products()
        print(f"Loaded {len(self.products)} products")
        for p in self.products:
            print(" -", getattr(p, "name", "???"))

        self.filtered_products = self.products.copy()
        self.category_filter = tk.StringVar(value="All")
        self.sort_by = tk.StringVar(value="Name (A-Z)")

        self.create_widgets()
        self.display_products()

    def create_widgets(self):
        filter_frame = tk.Frame(self)
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(filter_frame, text="Category:").pack(side="left")
        categories = ["All"] + sorted(set(getattr(p, "category", "Unknown") for p in self.products))
        tk.OptionMenu(filter_frame, self.category_filter, *categories, command=self.apply_filters).pack(side="left", padx=5)

        tk.Label(filter_frame, text="Sort by:").pack(side="left", padx=10)
        sort_options = ["Name (A-Z)", "Name (Z-A)", "Price (Low-High)", "Price (High-Low)"]
        tk.OptionMenu(filter_frame, self.sort_by, *sort_options, command=self.apply_filters).pack(side="left")

        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self.product_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.product_frame, anchor="nw")

    def apply_filters(self, *args):
        category = self.category_filter.get()
        if category == "All":
            self.filtered_products = self.products.copy()
        else:
            self.filtered_products = [p for p in self.products if getattr(p, "category", "") == category]

        sort_option = self.sort_by.get()
        if sort_option == "Name (A-Z)":
            self.filtered_products.sort(key=lambda x: x.name)
        elif sort_option == "Name (Z-A)":
            self.filtered_products.sort(key=lambda x: x.name, reverse=True)
        elif sort_option == "Price (Low-High)":
            self.filtered_products.sort(key=lambda x: float(x.price))
        elif sort_option == "Price (High-Low)":
            self.filtered_products.sort(key=lambda x: float(x.price), reverse=True)

        self.display_products()

    def display_products(self):
        for widget in self.product_frame.winfo_children():
            widget.destroy()

        for product in self.filtered_products:
            self.display_product(product)

    def display_product(self, product):
        frame = tk.Frame(self.product_frame, bd=1, relief="solid", padx=10, pady=5)
        frame.pack(fill="x", padx=10, pady=5)

        name = getattr(product, "name", "No Name")
        category = getattr(product, "category", "Unknown")
        price = getattr(product, "price", "0.00")

        tk.Label(frame, text=f"{name} | {category} | €{price}").pack(side="left")
        tk.Button(frame, text="Add to Cart", command=lambda: self.cart.append(product)).pack(side="right")

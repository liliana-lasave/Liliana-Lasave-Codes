import tkinter as tk

from tkinter import ttk

from catalogue_frame import CatalogueFrame  # Import safe: no circular


class CartFrame(ttk.Frame):
    """

    Shows all items currently in the cart and lets the user

    go back to the catalogue or forward to the checkout.

    """

    def __init__(self, master, app):
        super().__init__(master, padding=10)

        self.app = app

        ttk.Label(self, text="Shopping Cart", font=("Arial", 16, "bold")).pack(pady=10)

        # ---------- Listbox with cart items ----------

        self.lb = tk.Listbox(self, width=60)

        self.lb.pack(pady=5, fill="x")

        # Info: empty or X items

        self.info = ttk.Label(self)

        self.info.pack()

        # Total label

        self.total_lbl = ttk.Label(self, font=("Arial", 12, "bold"))

        self.total_lbl.pack()

        self.refresh()

        # ---------- Navigation buttons ----------

        nav = ttk.Frame(self)

        nav.pack(pady=10)

        # Back to catalogue (no circular import problem)

        ttk.Button(

            nav,

            text="Back",

            command=lambda: app.show_frame(CatalogueFrame)

        ).pack(side="left", padx=5)

        # Forward to checkout (lazy import to avoid circular reference)

        ttk.Button(

            nav,

            text="Checkout",

            command=lambda: app.show_frame(

                __import__("checkout_frame").CheckoutFrame

            )

        ).pack(side="left", padx=5)

    # --------------------------------------------------

    def refresh(self):
        """Refreshes listbox, info text and total amount."""

        self.lb.delete(0, tk.END)

        total = 0

        for item in self.app.cart:
            self.lb.insert(

                tk.END,

                f"{item['name']} x{item['quantity']}  €{item['price'] * item['quantity']:.2f}"

            )

            total += item["price"] * item["quantity"]

        msg = "Cart is empty" if total == 0 else f"{len(self.app.cart)} item(s) in cart"

        self.info.config(text=msg)

        self.total_lbl.config(text=f"Total: €{total:.2f}")


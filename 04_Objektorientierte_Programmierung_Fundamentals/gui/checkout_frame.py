import tkinter as tk

from tkinter import ttk

from cart_frame import CartFrame

import payment_frame as pf  # import alias to avoid circular


class CheckoutFrame(ttk.Frame):
    """Pantalla de revisión final antes de pagar"""

    def __init__(self, master, app):
        super().__init__(master, padding=10)

        self.app = app

        ttk.Label(self, text="Checkout", font=("Arial", 16, "bold")).pack(pady=10)

        subtotal = sum(i["price"] * i["quantity"] for i in app.cart)

        is_co = app.current_user and app.current_user["is_company"]

        discount = 0.05 * subtotal if is_co else 0

        self.total = subtotal - discount

        if is_co:
            ttk.Label(

                self,

                text=f"Company discount 5%: –€{discount:.2f}",

                foreground="green"

            ).pack()

        ttk.Label(

            self,

            text=f"Total to pay: €{self.total:.2f}",

            font=("Arial", 12, "bold")

        ).pack(pady=5)

        nav = ttk.Frame(self)

        nav.pack(pady=10)

        ttk.Button(

            nav, text="Back",

            command=lambda: app.show_frame(CartFrame)

        ).pack(side="left", padx=5)

        ttk.Button(

            nav, text="Next",

            command=lambda: app.show_frame(pf.PaymentFrame, total=self.total)

        ).pack(side="left", padx=5)


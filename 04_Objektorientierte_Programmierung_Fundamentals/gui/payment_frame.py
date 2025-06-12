import tkinter as tk

from tkinter import ttk, messagebox

from thankyou_frame import ThankYouFrame  # esta importación no genera ciclo


class PaymentFrame(ttk.Frame):
    """

    Payment step of the wizard.

    Allows the user to pick a method and finishes the order.

    """

    def __init__(self, master, app, total: float):

        super().__init__(master, padding=10)

        self.app = app

        self.total = total

        ttk.Label(self, text="Payment", font=("Arial", 16, "bold")).pack(pady=10)

        # --- select method ---

        self.method = tk.StringVar(value="Card")

        for label, code in [

            ("Credit Card", "Card"),

            ("PayPal", "PayPal"),

            ("Klarna / Sofort", "Klarna"),

            ("EPS Online Banking", "EPS")

        ]:
            ttk.Radiobutton(self, text=label, variable=self.method, value=code).pack(anchor="w")

        # --- cardholder field (only for credit card) ---

        self.card_label = ttk.Label(self, text="Cardholder name")

        self.card_entry = ttk.Entry(self)

        self.method.trace_add("write", self._toggle_cardholder)

        self._toggle_cardholder()

        # --- navigation buttons ---

        nav = ttk.Frame(self);
        nav.pack(pady=10)

        # BACK: import CheckoutFrame lazily to avoid circular import

        ttk.Button(

            nav, text="Back",

            command=lambda: app.show_frame(

                __import__("checkout_frame").checkout_frame.CheckoutFrame

            )

        ).pack(side="left", padx=5)

        ttk.Button(nav, text="Pay", command=self._pay).pack(side="left", padx=5)

    # --------------------------------------------------

    def _toggle_cardholder(self, *_):

        """Show Cardholder entry only for credit-card payments."""

        if self.method.get() == "Card":

            self.card_label.pack()

            self.card_entry.pack(fill="x")

        else:

            self.card_label.pack_forget()

            self.card_entry.pack_forget()

    # --------------------------------------------------

    def _pay(self):

        """

        Finalize the order and switch to thank-you screen

        with a personalized message for any payment method.

        """

        # Prefer cardholder entry; fallback to session username

        typed_name = self.card_entry.get().strip()

        base_name = typed_name or self.app.current_user["username"]

        # Add prefix for company customers

        is_company = self.app.current_user and self.app.current_user["is_company"]

        receiver_name = f"Company {base_name}" if is_company else base_name

        # Save order in DB

        oid = self.app.storage.save_order(

            self.app.cart,

            self.app.current_user["id"],

            is_company,

            self.method.get(),

            self.total

        )

        # Clear cart and persist empty state

        self.app.cart.clear()

        self.app.storage.save_cart(self.app.cart)

        # Show thank-you screen

        from thankyou_frame import ThankYouFrame

        self.app.show_frame(

            ThankYouFrame,

            receiver=receiver_name,

            method=self.method.get(),

            oid=oid

        )


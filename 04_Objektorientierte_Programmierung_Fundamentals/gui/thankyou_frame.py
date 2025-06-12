import tkinter as tk

from tkinter import ttk

from catalogue_frame import CatalogueFrame


class ThankYouFrame(ttk.Frame):
    """

    Final step of the checkout wizard.

    Shows a personalized thank-you message and a button

    to return to the catalogue.

    """

    def __init__(self, master, app, receiver: str, method: str, oid: int):
        super().__init__(master, padding=10)

        # ---------- Message strings (English) ----------

        header = f"Thank you for your purchase, {receiver}! 🎶"

        body = (

            "We will email your invoice shortly and our team will contact "

            "you to arrange the final details.\n"

            "Enjoy your classes!"

        )

        order = f"Order no.: {oid}   |   Payment: {method}"

        # ---------- Layout ----------

        ttk.Label(self, text=header, font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self, text=body, wraplength=500, justify="center").pack(pady=5)

        ttk.Label(self, text=order, font=("Arial", 10)).pack(pady=5)

        ttk.Button(

            self,

            text="Back to catalogue",

            command=lambda: app.show_frame(CatalogueFrame)

        ).pack(pady=10)



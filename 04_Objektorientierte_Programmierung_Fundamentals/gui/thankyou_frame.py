
from tkinter import ttk
from catalogue_frame import CatalogueFrame

class ThankYouFrame(ttk.Frame):
    def __init__(self, master, app, receiver, method, oid):
        super().__init__(master, padding=10)
        ttk.Label(self, text='Thank you!', font=('Arial',16,'bold')).pack(pady=10)
        ttk.Label(self, text=f'Thank you for your purchase, {receiver}!').pack(pady=5)
        ttk.Label(self, text=f'Payment method: {method}').pack()
        ttk.Label(self, text=f'Order number: {oid}').pack(pady=5)
        ttk.Button(self, text='Back to catalogue', command=lambda: app.show_frame(CatalogueFrame)).pack(pady=10)

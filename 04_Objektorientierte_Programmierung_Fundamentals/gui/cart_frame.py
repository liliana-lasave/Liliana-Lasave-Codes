
import tkinter as tk
from tkinter import ttk
def _catalogue_frame():
    mod = __import__('catalogue_frame')
    return getattr(mod, 'catalogue_frame', mod).CatalogueFrame if hasattr(mod, 'catalogue_frame') else mod.CatalogueFrame

class CartFrame(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app=app
        ttk.Label(self, text='Shopping Cart', font=('Arial',16,'bold')).pack(pady=10)
        self.lb=tk.Listbox(self,width=60); self.lb.pack(pady=5,fill='x')
        self.refresh()

        nav=ttk.Frame(self); nav.pack(pady=10)
        ttk.Button(nav,text='Back',command=lambda: app.show_frame(_catalogue_frame())).pack(side='left',padx=5)
        ttk.Button(nav,text='Checkout',command=lambda: app.show_frame(__import__('checkout_frame').checkout_frame.CheckoutFrame if hasattr(__import__('checkout_frame'),'checkout_frame') else __import__('checkout_frame').CheckoutFrame)).pack(side='left',padx=5)

    def refresh(self):
        self.lb.delete(0, tk.END)
        total=0
        for it in self.app.cart:
            self.lb.insert(tk.END,f"{it['name']} x{it['quantity']}  €{it['price']*it['quantity']:.2f}")
            total+=it['price']*it['quantity']
        ttk.Label(self,text=f"Total: €{total:.2f}",font=('Arial',12,'bold')).pack()

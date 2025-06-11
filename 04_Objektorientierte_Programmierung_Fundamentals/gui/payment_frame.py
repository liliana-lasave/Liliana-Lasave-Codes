
import tkinter as tk
from tkinter import ttk, messagebox
def _checkout_frame():
    mod=__import__('checkout_frame')
    return getattr(mod,'checkout_frame',mod).CheckoutFrame if hasattr(mod,'checkout_frame') else mod.CheckoutFrame
def _thankyou_frame():
    mod=__import__('thankyou_frame')
    return getattr(mod,'thankyou_frame',mod).ThankYouFrame if hasattr(mod,'thankyou_frame') else mod.ThankYouFrame

class PaymentFrame(ttk.Frame):
    def __init__(self, master, app, total):
        super().__init__(master, padding=10)
        self.app=app; self.total=total
        ttk.Label(self,text='Payment',font=('Arial',16,'bold')).pack(pady=10)
        self.method=tk.StringVar(value='Card')
        for lbl,val in [('Credit Card','Card'),('PayPal','PayPal'),('Klarna','Klarna'),('EPS','EPS')]:
            ttk.Radiobutton(self,text=lbl,variable=self.method,value=val).pack(anchor='w')

        self.card_label=ttk.Label(self,text='Cardholder name'); self.card_entry=ttk.Entry(self)
        self.method.trace_add('write', self.toggle); self.toggle()

        nav=ttk.Frame(self); nav.pack(pady=10)
        ttk.Button(nav,text='Back',command=lambda: app.show_frame(_checkout_frame())).pack(side='left',padx=5)
        ttk.Button(nav,text='Pay',command=self.pay).pack(side='left',padx=5)

    def toggle(self,*_):
        if self.method.get()=='Card':
            self.card_label.pack(); self.card_entry.pack(fill='x')
        else:
            self.card_label.pack_forget(); self.card_entry.pack_forget()

    def pay(self):
        name=self.card_entry.get().strip() or 'Customer'
        is_co=self.app.current_user and self.app.current_user['is_company']
        oid=self.app.storage.save_order(self.app.cart,self.app.current_user['id'],is_co,self.method.get(),self.total)
        self.app.cart.clear(); self.app.storage.save_cart(self.app.cart)
        self.app.show_frame(_thankyou_frame(), receiver=name, method=self.method.get(), oid=oid)

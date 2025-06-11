
import tkinter as tk
from tkinter import ttk, messagebox

CATEGORIES = {
    'All': None,
    'Private Lessons': 'private_lessons',
    'Group Workshops': 'group_workshops',
    'Courses': 'courses'
}

class CatalogueFrame(ttk.Frame):
    """Scrollable catalogue with category filter and sorting."""

    def __init__(self, master, app):
        super().__init__(master, padding=10)
        self.app = app
        self.filter_var = tk.StringVar(value='All')
        self.sort_var = tk.StringVar(value='Name')

        # Controls
        ctrl = ttk.Frame(self)
        ctrl.pack(fill='x')
        ttk.Label(ctrl, text='Category:').pack(side='left')
        ttk.Combobox(ctrl, textvariable=self.filter_var, values=list(CATEGORIES.keys()), state='readonly', width=18).pack(side='left', padx=5)

        ttk.Label(ctrl, text='Sort by:').pack(side='left', padx=(20,0))
        ttk.Combobox(ctrl, textvariable=self.sort_var, values=['Name','Price'], state='readonly', width=10).pack(side='left', padx=5)

        ttk.Button(ctrl, text='Apply', command=self.refresh).pack(side='left', padx=10)

        # Scrollable canvas
        canvas = tk.Canvas(self, highlightthickness=0)
        vsb = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        self.list_frame = ttk.Frame(canvas)
        self.list_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0,0), window=self.list_frame, anchor='nw')
        canvas.configure(yscrollcommand=vsb.set)
        canvas.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')

        ttk.Label(self, text='Product catalogue', font=('Arial',16,'bold')).pack(pady=10)
        self.refresh()

    def _filtered_sorted(self):
        prods = self.app.storage.load_all_products()
        cat = CATEGORIES[self.filter_var.get()]
        if cat:
            prods = [p for p in prods if p['table']==cat]
        prods.sort(key=lambda p: (p['price'] if self.sort_var.get()=='Price' else p['name'].lower()))
        return prods

    def refresh(self):
        for w in self.list_frame.winfo_children():
            w.destroy()
        for p in self._filtered_sorted():
            row=ttk.Frame(self.list_frame, padding=4); row.pack(fill='x', pady=2)
            ttk.Label(row, text=p['name'], width=40, anchor='w').pack(side='left')
            ttk.Label(row, text=f"€{p['price']:.2f}").pack(side='left', padx=10)
            ttk.Button(row, text='Add to cart', command=lambda prod=p: self.add(prod)).pack(side='right')

    def add(self, product):
        for it in self.app.cart:
            if it['table']==product['table'] and it['id']==product['id']:
                it['quantity']+=1; break
        else:
            self.app.cart.append({**product,'quantity':1})
        self.app.storage.save_cart(self.app.cart)
        messagebox.showinfo('Added','Item added to cart')

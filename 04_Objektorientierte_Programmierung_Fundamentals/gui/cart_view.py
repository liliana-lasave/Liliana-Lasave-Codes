import tkinter as tk
from tkinter import messagebox
from shared_cart import CART, remove_from_cart, clear_cart, get_cart_items
from order_view import open_order_dialog

# This function displays the cart items in a new window
def open_cart_view():
    window = tk.Toplevel()
    window.title("Shopping Cart")

    # Listbox to show the cart items
    listbox = tk.Listbox(window, width=50)
    listbox.pack(padx=10, pady=10)

    # Fill the listbox with product names
    for item in CART:
        listbox.insert(tk.END, item["name"])

    # Remove selected item from cart
    def remove_item():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            del CART[index]
            listbox.delete(index)

    remove_button = tk.Button(window, text="Remove Selected", command=remove_item)
    remove_button.pack(pady=5)

    # Proceed to checkout
    def proceed_to_checkout():
        window.destroy()
        open_order_dialog()

    checkout_button = tk.Button(window, text="Proceed to Checkout", command=proceed_to_checkout)
    checkout_button.pack(pady=5)

import tkinter as tk
from tkinter import ttk, messagebox
from shared_cart import CART, clear_cart  # Reuse the same cart list and clear function

def show_order(container):
    """
    Display the checkout view where the user reviews the cart,
    selects a delivery method, and confirms the order.
    """
    clear(container)

    # Title of the page
    ttk.Label(container, text="Checkout", font=("Helvetica", 16)).pack(pady=10)
    if not CART:

        # If the cart is empty, inform the user
        ttk.Label(container, text="Your cart is empty. Please add products before checking out.").pack()
        return

    # Create a frame to hold the list of cart items
    summary_frame = ttk.Frame(container)
    summary_frame.pack(fill="x", padx=10)

    # Show each item in the cart
    total_price = 0
    for product in CART:
        total_price += product["price"]
        item = ttk.Frame(summary_frame, padding=5)
        item.pack(fill="x")
        ttk.Label(item, text=f"{product['name']} - ${product['price']}").pack(anchor="w")

    # Display the subtotal
    ttk.Label(container, text=f"Total: ${total_price}", font=("Helvetica", 12, "bold")).pack(pady=10)

    # Delivery method selection
    ttk.Label(container, text="Choose delivery method:").pack()
    delivery_method = tk.StringVar(value="Standard")
    ttk.Radiobutton(container, text="Standard Delivery (Free)", variable=delivery_method, value="Standard").pack()
    ttk.Radiobutton(container, text="Express Delivery (+$10)", variable=delivery_method, value="Express").pack()

    # Confirm order button
    ttk.Button(
        container,
        text="Confirm Order",
        command=lambda: confirm_order(total_price, delivery_method.get())
    ).pack(pady=15)

def confirm_order(total, delivery):
    """
    Display order confirmation and clear the cart.
    """

    # Add delivery cost if express is selected
    if delivery == "Express":
        total += 10

    # Display a summary of the order
    summary = f"Order confirmed!\n\nDelivery Method: {delivery}\nTotal Price: ${total:.2f}"
    print(summary)
    messagebox.showinfo("Order Complete", summary)

    # Clear the cart after order
    CART.clear()


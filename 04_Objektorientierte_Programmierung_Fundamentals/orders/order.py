from datetime import datetime
from customers.customer_liliwelt import Customer
from products.products_liliwelt import Product


class Order:
    """
    A class to represent a completed order.
    It stores customer data, purchased products and total cost.
    It can generate an invoice as a .txt file.
    """

    def __init__(self, customer: Customer, products: list[Product], total: float):
        self.timestamp = datetime.now()
        self.customer_data = {
            "name": customer.name,
            "email": customer.email,
            "address": customer.address,
            "phone": customer.phone
        }
        self.products = products
        self.total_amount = total

    def calculate_total(self) -> float:
        """Return the total amount of the order."""
        return self.total_amount

    def generate_invoice(self, filename="invoice.txt"):
        """
        Generate a simple invoice as a text file, listing the customer data,
        all purchased products and the final amount.
        """
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"📄 Invoice - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("Customer Information:\n")
            f.write(f"Name: {self.customer_data['name']}\n")
            f.write(f"Email: {self.customer_data['email']}\n")
            f.write(f"Address: {self.customer_data['address']}\n")
            f.write(f"Phone: {self.customer_data['phone']}\n\n")
            f.write("Products:\n")
            for p in self.products:
                f.write(f"- {p.name}: €{p.price:.2f}\n")
            f.write(f"\nTotal Amount: €{self.total_amount:.2f}\n")
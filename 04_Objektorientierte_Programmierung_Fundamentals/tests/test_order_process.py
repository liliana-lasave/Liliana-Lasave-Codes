import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Print current sys.path to debug
print("sys.path:")
for p in sys.path:
    print(p)

# Check if the file exists
print("File exists?", os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'orders', 'order.py')))

from customers.company_customer_liliwelt import Company_customer
from products.products_liliwelt import PrivateLesson
from orders.shopping_cart import ShoppingCart
from orders.order import Order

# Create a company customer
customer = Company_customer(
    name="Lili Lasave",
    address="Hauptstraße 123",
    postcode="8010",
    locality="Graz",
    email="lili@example.com",
    phone="06641234567",
    password="SecurePass123",
    company_number="123456789"
)

# Create a sample product

product = PrivateLesson(
    name="Private Singing Lesson",
    price=60.0,
    duration="1 hour",
    level="Beginner",
    audience="Teens",
    modality="Online",
    teacher_name="Lili",
    instrument="Voice"
)

# Add product to the shopping cart
cart = ShoppingCart(customer)
cart.add_product(product)
print("🛒 Shopping cart total:", cart.total)

# Create an order from the cart
order = Order(customer, cart.products, cart.total)

# Generate the invoice
order.generate_invoice("invoice_test.txt")
print("Invoice generated as 'invoice_test.txt'")
print("Order total:", order.calculate_total())


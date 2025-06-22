from products.products_liliwelt import Product
from customers.customer_liliwelt import Customer
from customers.company_customer_liliwelt import Company_customer  # ← uso correcto del nombre


class ShoppingCart:
    """
    A class to manage the shopping cart for a customer.
    It temporarily holds products and calculates the total cost,
    including an automatic 5% discount for company customers.
    """

    def __init__(self, customer: Customer):
        self.customer = customer
        self.products = []  # List of selected products
        self.total = 0.0  # Total cost of products in cart

    def add_product(self, product: Product):
        """Add a product to the shopping cart and recalculate total."""
        self.products.append(product)
        self.calculate_total()

    def remove_product(self, product: Product):
        """Remove a product from the shopping cart and recalculate total."""

        if product in self.products:
            self.products.remove(product)
            self.calculate_total()

    def clear_cart(self):
        """Remove all products from the cart and reset the total."""
        self.products.clear()
        self.total = 0.0

    def calculate_total(self):
        """
        Calculate the total cost of all products in the cart.
        If the customer is a company customer, apply a 5% discount.
        """

        self.total = sum(p.price for p in self.products)
        if isinstance(self.customer, Company_customer):  # ← nombre correcto
            self.total *= 0.95


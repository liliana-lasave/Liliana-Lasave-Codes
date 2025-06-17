# shopping_cart.py

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product_id, name, quantity):
        """
        Adds an item to the cart. If the product is already in the cart, update its quantity.
        """
        for item in self.items:
            if item["product_id"] == product_id:
                item["quantity"] += quantity
                return
        self.items.append({"product_id": product_id, "name": name, "quantity": quantity})

    def remove_item(self, product_id):
        """
        Removes an item from the cart by product_id.
        """
        self.items = [item for item in self.items if item["product_id"] != product_id]

    def clear_cart(self):
        """
        Empties the cart.
        """
        self.items.clear()

    def get_items(self):
        """
        Returns the list of items currently in the cart.
        """
        return self.items

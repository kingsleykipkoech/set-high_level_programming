"""
Refactored Object-Oriented Product Inventory Manager
Integrated with @property setters, data validation, and custom exceptions.
"""


class InvalidProductDataError(Exception):
    """Custom exception raised when product data validation fails."""
    pass


class Product:
    """Represents a product with a name, price, and quantity."""

    def __init__(self, name, price, quantity):
        """Initializes Product attributes, delegating validation."""
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        """Retrieves the price of the product."""
        return self._price

    @price.setter
    def price(self, value):
        """Sets the price with validation for positive numeric values."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise InvalidProductDataError(
                f"Price must be a number, got {type(value).__name__}."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Price cannot be negative, got {value}."
            )
        self._price = float(value)

    @property
    def quantity(self):
        """Retrieves the quantity of the product."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Sets the quantity with validation for non-negative integers."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidProductDataError(
                f"Quantity must be an integer, got {type(value).__name__}."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Quantity cannot be negative, got {value}."
            )
        self._quantity = value


class InventoryManager:
    """Manages the collection of products and provides operations."""

    def __init__(self, inventory=None):
        """Initializes the inventory list."""
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product):
        """Adds a product object to the inventory list."""
        self.inventory.append(product)

    def update_quantity(self, name, new_quantity):
        """Updates the quantity of a product by name."""
        for product in self.inventory:
            if product.name == name:
                product.quantity = new_quantity
                break

    def calculate_total_value(self):
        """Calculates the total monetary value of all inventory."""
        total = 0
        for product in self.inventory:
            total += product.price * product.quantity
        return total

    def display_inventory(self):
        """Prints the current inventory list."""
        for product in self.inventory:
            fmt = f"{product.name} - ${product.price:.2f} x {product.quantity}"
            print(fmt)


# Demo Usage & Edge Case Testing
if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_product(Product("Laptop", 1200.00, 5))
    manager.add_product(Product("Mouse", 25.00, 20))
    manager.update_quantity("Mouse", 18)

    print("Current Inventory:")
    manager.display_inventory()
    print(f"\nTotal Inventory Value: ${manager.calculate_total_value():.2f}")

    # --- Testing Invalid Input ---
    print("\n--- Testing Invalid Input ---")
    try:
        manager.inventory[0].quantity = -5
    except Exception as e:
        print(f"Test result: {e}")

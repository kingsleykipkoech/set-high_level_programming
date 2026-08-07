# Refactored Object-Oriented Product Inventory Manager (With Data Validation)


class InvalidProductDataError(Exception):
    """Custom exception raised when product data validation fails."""
    pass


class Product:
    """Represents a product with a name, price, and quantity."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price        # Triggers price.setter validation
        self.quantity = quantity  # Triggers quantity.setter validation

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise InvalidProductDataError(
                f"Price must be a non-negative number (got {type(value).__name__}: {value!r})."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Price cannot be negative (got {value})."
            )
        self._price = float(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise InvalidProductDataError(
                f"Quantity must be a non-negative integer (got {type(value).__name__}: {value!r})."
            )
        if value < 0:
            raise InvalidProductDataError(
                f"Quantity cannot be negative (got {value})."
            )
        self._quantity = value


class InventoryManager:
    """Manages the collection of products and provides inventory operations."""

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add_product(self, product):
        """Adds a product object to the inventory list."""
        self.inventory.append(product)

    def update_quantity(self, name, new_quantity):
        """Updates the quantity of a product by name."""
        for product in self.inventory:
            if product.name == name:
                product.quantity = new_quantity  # Triggers quantity.setter validation
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
            print(f"{product.name} - ${product.price:.2f} x {product.quantity}")


# Demo Usage
if __name__ == "__main__":
    print("--- 1. Valid Product Creation & Operations ---")
    manager = InventoryManager()
    manager.add_product(Product("Laptop", 1200.00, 5))
    manager.add_product(Product("Mouse", 25.00, 20))
    manager.update_quantity("Mouse", 18)

    print("Current Inventory:")
    manager.display_inventory()
    print(f"Total Inventory Value: ${manager.calculate_total_value():.2f}\n")

    print("--- 2. Validation Testing ---")
    test_cases = [
        ("Negative Price", lambda: Product("Gadget", -10.00, 5)),
        ("Invalid Price Type", lambda: Product("Gadget", "invalid", 5)),
        ("Negative Quantity", lambda: Product("Gadget", 15.00, -3)),
        ("Float Quantity", lambda: Product("Gadget", 15.00, 4.5)),
        ("Update to Negative Quantity", lambda: manager.update_quantity("Mouse", -5)),
    ]

    for label, test in test_cases:
        try:
            test()
            print(f"[FAIL] {label}: No exception raised!")
        except InvalidProductDataError as e:
            print(f"[PASS] {label}: Caught InvalidProductDataError -> {e}")

    print("\n--- Testing Invalid Input ---")
    try:
        manager.inventory[0].quantity = -5
    except Exception as e:
        print(f"Test result: {e}")

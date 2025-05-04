class Product:
    """
    A class to represent a product in an inventory system.

    Attributes:
    - name (str): The name of the product.
    - price (float): The price per unit of the product (must be >= 0).
    - quantity (int): The quantity in stock (must be >= 0).

    Methods:
    - add_inventory(amount): Adds stock to the product quantity.
    - remove_inventory(amount): Removes stock from the product quantity.
    - total_value(): Returns total value of current inventory (price × quantity).
    - display_info(): Prints the product's information.

    Raises:
    - ValueError: If invalid inputs are provided for price, quantity, or inventory changes.
    """

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, amount: int):
        """
        Adds the specified amount to the product's inventory.

        Parameters:
        - amount (int): The quantity to add (must be >= 0).

        Raises:
        - ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative quantity.")
        self.quantity += amount

    def remove_inventory(self, amount: int):
        """
        Removes the specified amount from the product's inventory.

        Parameters:
        - amount (int): The quantity to remove (must be >= 0 and <= current quantity).

        Raises:
        - ValueError: If amount is negative or exceeds available stock.
        """
        if amount < 0:
            raise ValueError("Cannot remove a negative quantity.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more than available quantity.")
        self.quantity -= amount

    def total_value(self) -> float:
        """
        Calculates the total value of the product in inventory.

        Returns:
        - float: Total inventory value.
        """
        return self.price * self.quantity

    def display_info(self):
        """
        Displays the product's details.
        """
        print(f"Product: {self.name}")
        print(f"Price per unit: ${self.price:.2f}")
        print(f"Quantity in stock: {self.quantity}")
        print(f"Total value: ${self.total_value():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        item = Product("Notebook", 3.50, 100)
        item.display_info()
        print("\nAdding 20 items...")
        item.add_inventory(20)
        item.display_info()
        print("\nRemoving 50 items...")
        item.remove_inventory(50)
        item.display_info()
    except ValueError as e:
        print("Error:", e)
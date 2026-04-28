class Node:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price  # 0 for categories
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def calculate_total_price(root):
    # Base case
    if root is None:
        return 0

    total = root.price  # add current node price

    # Traverse children
    for child in root.children:
        total += calculate_total_price(child)

    return total


# Example Usage
if __name__ == "__main__":
    # Create tree structure
    cart = Node("Shopping Cart")

    electronics = Node("Electronics")
    groceries = Node("Groceries")

    laptop = Node("Laptop", 50000)
    phone = Node("Phone", 20000)

    apple = Node("Apple", 100)
    milk = Node("Milk", 50)

    # Build tree
    electronics.add_child(laptop)
    electronics.add_child(phone)

    groceries.add_child(apple)
    groceries.add_child(milk)

    cart.add_child(electronics)
    cart.add_child(groceries)

    # Calculate total
    total_price = calculate_total_price(cart)
    print("Total Price:", total_price)
def calculate_final_cost(items):
    subtotal = 0

    # Calculate subtotal after item-level discounts
    for price, discount_percent in items:
        item_cost = price - (price * discount_percent / 100)
        subtotal += item_cost

    percentage_discount = 0
    fixed_discount = 0

    # Apply overall discounts
    if subtotal > 500:
        percentage_discount = subtotal * 0.10

    if subtotal > 1000:
        fixed_discount = 150

    # Choose the maximum discount
    discount = max(percentage_discount, fixed_discount)

    final_cost = subtotal - discount

    return int(final_cost)


try:
    n = int(input("Enter number of items: "))

    data = list(map(int, input(
        "Enter price and discount for each item (price discount): "
    ).split()))

    if len(data) != 2 * n:
        raise ValueError("Incorrect number of values entered")

    # Create list of (price, discount_percent) tuples
    items = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]

    print("Final Cost:", calculate_final_cost(items))

except ValueError:
    print("Invalid input. Please enter numbers only.")

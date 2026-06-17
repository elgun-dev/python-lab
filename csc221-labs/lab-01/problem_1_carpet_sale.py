# Problem 1: Carpet Sale
# This program calculates carpet, labor, tax, and total sales for three orders.

# These constants store the rates used in every carpet order.
WASTE_RATE = 0.20
LABOR_RATE = 0.75
TAX_RATE = 0.07

# Read the first order from the user.
print("Enter order 1: carpet price per square foot, room width, and room length.")
print("Example: 0.95 12 12")
price_1, width_1, length_1 = input("Order 1: ").split()
price_1 = float(price_1)
width_1 = int(width_1)
length_1 = int(length_1)

# Read the second order from the user.
print("Enter order 2: carpet price per square foot, room width, and room length.")
print("Example: 1.25 8 18")
price_2, width_2, length_2 = input("Order 2: ").split()
price_2 = float(price_2)
width_2 = int(width_2)
length_2 = int(length_2)

# Read the third order from the user.
print("Enter order 3: carpet price per square foot, room width, and room length.")
print("Example: 1.12 10 17")
price_3, width_3, length_3 = input("Order 3: ").split()
price_3 = float(price_3)
width_3 = int(width_3)
length_3 = int(length_3)

# Calculate all values for order 1.
area_1 = width_1 * length_1
carpet_1 = price_1 * area_1 * (1 + WASTE_RATE)
labor_1 = area_1 * LABOR_RATE
tax_1 = (carpet_1 + labor_1) * TAX_RATE
cost_1 = carpet_1 + labor_1 + tax_1

# Calculate all values for order 2.
area_2 = width_2 * length_2
carpet_2 = price_2 * area_2 * (1 + WASTE_RATE)
labor_2 = area_2 * LABOR_RATE
tax_2 = (carpet_2 + labor_2) * TAX_RATE
cost_2 = carpet_2 + labor_2 + tax_2

# Calculate all values for order 3.
area_3 = width_3 * length_3
carpet_3 = price_3 * area_3 * (1 + WASTE_RATE)
labor_3 = area_3 * LABOR_RATE
tax_3 = (carpet_3 + labor_3) * TAX_RATE
cost_3 = carpet_3 + labor_3 + tax_3

# Add each order cost to get total sales.
total_sales = cost_1 + cost_2 + cost_3

# Display order 1.
print("Order #1")
print(f"Room: {area_1} sq ft")
print(f"Carpet: ${carpet_1:.2f}")
print(f"Labor: ${labor_1:.2f}")
print(f"Tax: ${tax_1:.2f}")
print(f"Cost: ${cost_1:.2f}")
print()

# Display order 2.
print("Order #2")
print(f"Room: {area_2} sq ft")
print(f"Carpet: ${carpet_2:.2f}")
print(f"Labor: ${labor_2:.2f}")
print(f"Tax: ${tax_2:.2f}")
print(f"Cost: ${cost_2:.2f}")
print()

# Display order 3.
print("Order #3")
print(f"Room: {area_3} sq ft")
print(f"Carpet: ${carpet_3:.2f}")
print(f"Labor: ${labor_3:.2f}")
print(f"Tax: ${tax_3:.2f}")
print(f"Cost: ${cost_3:.2f}")
print()

# Display the total for all three orders.
print(f"Total Sales: ${total_sales:.2f}")

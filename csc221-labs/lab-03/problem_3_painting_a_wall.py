from math import ceil

# Problem 3: Painting a Wall
# This program calculates paint needed and the final paint cost.

# These constants store the paint coverage and sales tax rate.
COVERAGE_PER_GALLON = 350.0
TAX_RATE = 0.07

# Read the wall height, wall width, and paint can cost.
print("Enter the wall height in feet.")
wall_height = float(input("Wall height: "))
print("Enter the wall width in feet.")
wall_width = float(input("Wall width: "))
print("Enter the cost of one paint can.")
can_cost = float(input("Paint can cost: "))

# Calculate the wall area in square feet.
wall_area = wall_height * wall_width

# Calculate the number of gallons needed for the wall.
paint_needed = wall_area / COVERAGE_PER_GALLON

# Round up because paint is purchased in full cans.
cans_needed = ceil(paint_needed)

# Calculate paint cost, sales tax, and total cost.
paint_cost = cans_needed * can_cost
sales_tax = paint_cost * TAX_RATE
total_cost = paint_cost + sales_tax

# Display all results.
print(f"Wall area: {wall_area:.1f} sq ft")
print(f"Paint needed: {paint_needed:.3f} gallons")
print(f"Cans needed: {cans_needed} can(s)")
print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")

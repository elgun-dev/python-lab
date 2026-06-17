import math

# Problem 2: Pizza Party
# This program calculates pizza costs for Friday, Saturday, and Sunday parties.

# These constants store pizza size and extra charge rates.
SLICES_PER_PIZZA = 8
TAX_RATE = 0.07
DELIVERY_RATE = 0.20

# Read the Friday party information.
print("Enter Friday party: number of people, average slices per person, and cost of one pizza.")
print("Example: 6 2.8 10.95")
people_fri, slices_fri, price_fri = input("Friday: ").split()
people_fri = int(people_fri)
slices_fri = float(slices_fri)
price_fri = float(price_fri)

# Read the Saturday party information.
print("Enter Saturday party: number of people, average slices per person, and cost of one pizza.")
print("Example: 22 2.1 12.95")
people_sat, slices_sat, price_sat = input("Saturday: ").split()
people_sat = int(people_sat)
slices_sat = float(slices_sat)
price_sat = float(price_sat)

# Read the Sunday party information.
print("Enter Sunday party: number of people, average slices per person, and cost of one pizza.")
print("Example: 12 1.8 14.95")
people_sun, slices_sun, price_sun = input("Sunday: ").split()
people_sun = int(people_sun)
slices_sun = float(slices_sun)
price_sun = float(price_sun)

# Calculate the Friday party cost.
pizzas_fri = math.ceil((people_fri * slices_fri) / SLICES_PER_PIZZA)
pizza_cost_fri = pizzas_fri * price_fri
tax_fri = pizza_cost_fri * TAX_RATE
delivery_fri = (pizza_cost_fri + tax_fri) * DELIVERY_RATE
total_fri = pizza_cost_fri + tax_fri + delivery_fri

# Calculate the Saturday party cost.
pizzas_sat = math.ceil((people_sat * slices_sat) / SLICES_PER_PIZZA)
pizza_cost_sat = pizzas_sat * price_sat
tax_sat = pizza_cost_sat * TAX_RATE
delivery_sat = (pizza_cost_sat + tax_sat) * DELIVERY_RATE
total_sat = pizza_cost_sat + tax_sat + delivery_sat

# Calculate the Sunday party cost.
pizzas_sun = math.ceil((people_sun * slices_sun) / SLICES_PER_PIZZA)
pizza_cost_sun = pizzas_sun * price_sun
tax_sun = pizza_cost_sun * TAX_RATE
delivery_sun = (pizza_cost_sun + tax_sun) * DELIVERY_RATE
total_sun = pizza_cost_sun + tax_sun + delivery_sun

# Add all party totals for the weekend total.
weekend_total = total_fri + total_sat + total_sun

# Display the Friday party information.
print("Friday Night Party")
print(f"{pizzas_fri} Pizzas: ${pizza_cost_fri:.2f}")
print(f"Tax: ${tax_fri:.2f}")
print(f"Delivery: ${delivery_fri:.2f}")
print(f"Total: ${total_fri:.2f}")
print()

# Display the Saturday party information.
print("Saturday Night Party")
print(f"{pizzas_sat} Pizzas: ${pizza_cost_sat:.2f}")
print(f"Tax: ${tax_sat:.2f}")
print(f"Delivery: ${delivery_sat:.2f}")
print(f"Total: ${total_sat:.2f}")
print()

# Display the Sunday party information.
print("Sunday Night Party")
print(f"{pizzas_sun} Pizzas: ${pizza_cost_sun:.2f}")
print(f"Tax: ${tax_sun:.2f}")
print(f"Delivery: ${delivery_sun:.2f}")
print(f"Total: ${total_sun:.2f}")
print()

# Display the total cost for the weekend.
print(f"Weekend Total: ${weekend_total:.2f}")

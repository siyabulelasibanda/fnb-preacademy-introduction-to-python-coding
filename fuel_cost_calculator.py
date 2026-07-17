# Ask the user for the distance and petrol price.
kilometers = float(input("How many kilometers will you drive? "))
petrol_price = float(input("Enter the petrol price per litre: R"))

# Calculate how many litres are needed (1 litre per 10 km).
litres_needed = kilometers / 10

# Calculate and round the total travel cost.
total_cost = round(litres_needed * petrol_price, 2)

print(f"Litres needed: {litres_needed}")
print(f"Total fuel cost: R{total_cost}")

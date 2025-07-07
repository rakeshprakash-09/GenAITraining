# Take input for the cost of three items
item1 = float(input("Enter the cost of item 1: "))
item2 = float(input("Enter the cost of item 2: "))
item3 = float(input("Enter the cost of item 3: "))

# Take input for the tax percentage
tax_percent = float(input("Enter the tax percentage: "))

# Calculate the total cost before tax
total_cost = item1 + item2 + item3

# Calculate the tax amount
tax_amount = total_cost * (tax_percent / 100)

# Calculate the final amount
final_amount = total_cost + tax_amount

# Print the final amount
print(f"Final amount to be paid (including tax): {final_amount:.2f}")


# Item prices and quantities
prices = [100, 200, 50]
quantities = [2, 1, 3]

# Discount and tax rates (in percentage)
discount_rate = 10
tax_rate = 5

# Calculate subtotal
subtotal = sum(price * quantity
               for price, quantity in zip(prices, quantities))

# Calculate discount
discount = subtotal * discount_rate / 100

# Apply discount
discounted_total = subtotal - discount

# Calculate tax
tax = discounted_total * tax_rate / 100

# Calculate final total
total_cost = discounted_total + tax

# Display results
print("Subtotal: ₹", round(subtotal, 2))
print("Discount: ₹", round(discount, 2))
print("Tax: ₹", round(tax, 2))
print("Final Total: ₹", round(total_cost, 2))

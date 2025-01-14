Total_selling_price = float(input("Enter the total selling price of 15 items: "))

Total_profit = float(input("Enter the total profit earned on 15 items: "))

Total_cost_price = Total_selling_price - Total_profit

Cost_price_per_item = Total_cost_price / 15

print(f"The cost price of one item is: {Cost_price_per_item:.2f}")

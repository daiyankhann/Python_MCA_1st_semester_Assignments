Cost_price = float(input("Enter the cost price of the item: "))
Selling_price = float(input("Enter the selling price of the item: "))

if Selling_price > Cost_price:
    Profit = Selling_price - Cost_price
    print(f"The seller has made a profit of Rs. {Profit}")
elif Selling_price < Cost_price:
    Loss = Cost_price - Selling_price
    print(f"The seller has incurred a loss of Rs. {Loss}")
else:
    print("The seller has neither made a profit nor incurred a loss")

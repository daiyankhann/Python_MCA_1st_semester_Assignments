def calculate_amount(p, r, n, q):
    a = p * (1 + r / (100 * q)) ** (q * n)
    return a

for i in range(10):
    print(f"Enter details for set {i+1}:")
    p = float(input("Principal amount (p): "))
    r = float(input("Annual interest rate (r in %): "))
    n = int(input("Number of years (n): "))
    q = int(input("Number of times interest compounds per year (q): "))
    
    a = calculate_amount(p, r, n, q)
    print(f"The compounded amount for set {i+1} is: {a:.2f}\n")
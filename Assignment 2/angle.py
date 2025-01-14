a1 = float(input("Enter the first angle of the triangle: "))
a2 = float(input("Enter the second angle of the triangle: "))
a3 = float(input("Enter the third angle of the triangle: "))

if a1 > 0 and a2 > 0 and a3 > 0 and (a1 + a2 + a3 == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

Length = float(input("Enter the length of the rectangle: "))
Breadth = float(input("Enter the breadth of the rectangle: "))

Area = Length * Breadth
Perimeter = 2 * (Length + Breadth)

if Area > Perimeter:
    print("Area of the rectangle is greater than its perimeter")
else:
    print("Area of the rectangle is not greater than its perimeter")
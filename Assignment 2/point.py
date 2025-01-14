x = float(input("Enter the x-coordinate of the point: "))
y = float(input("Enter the y-coordinate of the point: "))

if x == 0 and y == 0:
    print("The point lies at the origin (0, 0)")
elif x == 0:
    print("The point lies on the y-axis")
elif y == 0:
    print("The point lies on the x-axis")
else:
    print("The point does not lie on the x-axis, y-axis, or at the origin")

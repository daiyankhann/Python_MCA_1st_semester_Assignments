import math

x = float(input("Enter the x-coordinate of the center of the circle: "))
y = float(input("Enter the y-coordinate of the center of the circle: "))
r = float(input("Enter the radius of the circle: "))

xp = float(input("Enter the x-coordinate of the point: "))
yp = float(input("Enter the y-coordinate of the point: "))

distance = math.sqrt(pow(xp - x, 2) + pow(yp - y, 2))

if distance < r:
    print("The point is inside the circle.")
elif distance == r:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")

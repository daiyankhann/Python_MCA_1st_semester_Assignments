number_1 = float(input("Enter number 1: "))

number_2 = float(input("Enter number 2: "))

print("Before swapping")

print(f"number 1: {number_1}")

print(f"number 2: {number_2}")

number_1 = number_1 - number_2

number_2 = number_2 + number_1

number_1 = number_2 - number_1

print("After swapping")

print(f"number 1: {number_1}")

print(f"number 2: {number_2}")
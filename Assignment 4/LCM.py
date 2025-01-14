def calculate_lcm(a, b):
    lcm = max(a, b)
    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


lcm = calculate_lcm(num1, num2)
print(f"The L.C.M. of {num1} and {num2} is: {lcm}")
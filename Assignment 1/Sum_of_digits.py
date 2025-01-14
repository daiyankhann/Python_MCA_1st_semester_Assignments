number = int(input("Enter the number: "))

sum = 0

while(number != 0):
    r = number % 10
    sum = sum + r
    number //= 10

print(f"Sum of the digits of a number: {sum}")
number = int(input("Enter the number: "))

reverse = 0

while(number != 0):
    r = number % 10
    reverse = (reverse * 10) + r
    number //= 10

print(f"Reverse the number: {reverse}")
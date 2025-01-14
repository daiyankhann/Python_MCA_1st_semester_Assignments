number = int(input("Enter a number(Only four digits): "))

last = number % 10

first = number // 1000

sum_of_digits = first + last

print(f"Sum of the first and last digit: {sum_of_digits}")

number = input("Enter a five-digit number: ")

new_number = ""

for digit in number:
    new_digit = str((int(digit) + 1) % 10)  
    new_number += new_digit

print(f"The new number is: {new_number}")

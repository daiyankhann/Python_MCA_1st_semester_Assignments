decimal_number = int(input("Enter a decimal number: "))
original_number = decimal_number  

        
if decimal_number == 0:
    print("The octal equivalent of 0 is 0")

octal_number = ""
while decimal_number > 0:
        remainder = decimal_number % 8
        octal_number = str(remainder) + octal_number
        decimal_number //= 8
print(f"The octal equivalent of {original_number} is {octal_number}")
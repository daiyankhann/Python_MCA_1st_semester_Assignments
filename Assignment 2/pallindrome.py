Number = input("Enter a number: ")

if len(Number) != 5 or not Number.isdigit():
    print("Invalid input! Please enter a five-digit number.")
else:
    Reversed_number = Number[::-1]

    if Number == Reversed_number:
        print("Number is pallindrome")
    else:
        print("Number is not pallindrome")
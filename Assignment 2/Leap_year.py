Year = int(input("Enter a year: "))

if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print(f"The year {Year} is a leap year")
else:
    print(f"The year {Year} is not a leap year.")

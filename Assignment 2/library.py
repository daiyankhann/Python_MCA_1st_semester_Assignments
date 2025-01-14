Days_late = int(input("Enter the number of days late to return the book: "))

if Days_late > 30:
    print("Membership cancelled, You have returned the book after 30 days")
elif Days_late > 10:
    fine = (Days_late - 10) * 5 + 5 * 1  
    print(f"The fine is {fine} rupees")
elif Days_late >= 6:
    fine = (Days_late - 5) * 1 + 5 * 0.50  
    print(f"The fine is {fine} rupees")
elif Days_late >= 1:
    fine = Days_late * 0.50  
    print(f"The fine is {fine} rupees")
else:
    print("No fine, Book returned on time")
Amount = int(input("Enter the amount to be withdrawn: "))


if Amount % 10 != 0:
    print("Invalid amount. Please enter a valid amount in multiples of 10.")
else:
    notes_100 = Amount // 100  

    remaining = Amount % 100   
    
    notes_50 = remaining // 50

    remaining = remaining % 50 
    
    notes_10 = remaining // 10 

    print(f"Number of 100 currency notes: {notes_100}")

    print(f"Number of 50 currency notes: {notes_50}")

    print(f"Number of 10 currency notes: {notes_10}")

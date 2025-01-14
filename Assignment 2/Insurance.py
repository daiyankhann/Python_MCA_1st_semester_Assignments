Health = input("Enter health status (excellent/poor): ")
Age = int(input("Enter the age of the person: "))
Location = input("Enter the location (city/village): ")
Sex = input("Enter the sex (male/female): ")


if Health == "excellent" and 25 <= Age <= 35 and Location == "city" and Sex == "male":
    Premium_rate = 4 
    Max_amount = 200000 
    print("The person should be insured")
    print(f"Premium rate: Rs. {Premium_rate} per thousand")
    print(f"Maximum insured amount: Rs {Max_amount}")
    
elif Health == "excellent" and 25 <= Age <= 35 and Location == "city" and Sex == "female":
    Premium_rate = 3  
    Max_amount = 100000  
    print("The person should be insured")
    print(f"Premium rate: Rs. {Premium_rate} per thousand")
    print(f"Maximum insured amount: Rs {Max_amount}")
    
elif Health == "poor" and 25 <= Age <= 35 and Location == "village" and Sex == "male":
    Premium_rate = 6  
    Max_amount = 10000  
    print("The person should be insured")
    print(f"Premium rate: Rs. {Premium_rate} per thousand.")
    print(f"Maximum insured amount: Rs {Max_amount}")
    
else:
    print("The person is not eligible for insurance")

Ram = int(input("Enter Ram's age: "))
Shyam = int(input("Enter Shyam's age: "))
Ajay = int(input("Enter Ajay's age: "))

if Ram < Shyam and Ram < Ajay:
    print("Ram is the youngest")
elif Shyam < Ram and Shyam < Ajay:
    print("Shyam is the youngest")
elif Ajay < Ram and Ajay < Shyam:
    print("Ajay is the youngest")
else:
    print("There is a tie for the youngest age")

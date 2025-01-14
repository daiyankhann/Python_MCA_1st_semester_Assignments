Year = int(input("Enter a year: "))

y = 1900
d = 0  
w = 7
Days = 0

if Year >= y:
    for i in range(y, Year):
        if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):  
            Days += 366
        else:
            Days += 365
else:
    for j in range(Year, y):
        if (j % 4 == 0 and (j % 100 != 0 or j % 400 == 0)):  
            Days -= 366
        else:
            Days -= 365

w = (d + Days) % w

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(f"January 1, {Year} is a {days[w]}.")

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n=1
for i in range(0,n2):
    n *= n1
print("The value of one number raised to the power of another is : ",n)
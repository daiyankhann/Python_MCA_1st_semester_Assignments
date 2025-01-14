def factorial(n):
    f=1
    while n > 0:
        f =f*n
        n-=1
    return f
sum=0
num= int(input("Enter the number of terms: "))
for i in range(1,num+1):
    sum = sum+ i/factorial(i)
print("Sum of the terms :",sum)
def factorial(a):
    f=1
    while a > 0:
        f =f*a
        a-=1
    return f
def Combinatoric(x,y):
    res= (factorial(x)/(factorial(y)*factorial(x-y)))
    return res
n=int(input("Enter N in Combinatoric C(n,r) : "))
r=int(input("Enter R in Combinatoric C(n,r) : "))
print("The calculation of Combinatoric C(n,r) : ",Combinatoric(n,r))
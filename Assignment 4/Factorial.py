def factorial(a):
    f=1
    while a > 0:
        f =f*a
        a-=1
    return f
num = int(input("Enter a natural number : "))
print(f"Factorial of {num} is :",factorial(num))
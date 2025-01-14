def fibonacci_sum(n):
    
    a, b = 0, 1
    total_sum = a  
    for _ in range(1, n): 
        total_sum += b
        a, b = b, a + b

    return total_sum
n = int(input("Enter the number of terms in the Fibonacci series: "))

result = fibonacci_sum(n)
print(f"The sum of the first {n} terms of the Fibonacci series is: {result}")
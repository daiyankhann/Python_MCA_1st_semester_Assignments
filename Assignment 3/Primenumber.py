for num in range(1, 301):
  if num >1 :
    is_prime = True 
    for i in range(2, num//2 + 1): 
        if num % i == 0:
            is_prime = False  
            break  

    
    if not is_prime:
        continue

    print(num, end=" ")
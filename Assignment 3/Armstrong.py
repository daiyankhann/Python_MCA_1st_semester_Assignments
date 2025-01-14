def Armstrong(Number):
  sum=0
  temp=Number
  while temp > 0:
    digit = temp % 10
    sum +=digit**3
    temp //=10
  return sum==Number
print("Armstrong numbers between 1 and 500 are:") 
for num in range(1,501):
       if Armstrong(num):
        print(num) 
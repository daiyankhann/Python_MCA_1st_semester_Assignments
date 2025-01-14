numbers = [1, 2, 3]
count=0
print("All combinations of 1, 2, and 3:")
for i in numbers:
    for j in numbers:
        for k in numbers:
            count +=1
            print(i, j, k)
print("Number of Total Combinations: ",count)
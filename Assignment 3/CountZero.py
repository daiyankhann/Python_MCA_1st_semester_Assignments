czero=0
cneg=0
cpos=0
while True:
 n=(input("Enter a Number(Type 'stop' to Finish) :"))
 if n.lower() == 'stop':
     break
 n=float(n)
 if n == 0:
    czero +=1
 elif n > 0:
    cpos +=1
 else:
    cneg +=1
print("Number of Zero :",czero)
print("Number of Negetive Numbers:",cneg)
print("Number of Positive Numbers:",cpos)
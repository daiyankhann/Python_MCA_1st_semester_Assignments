A = float(input("Enter the length of side A: "))
B = float(input("Enter the length of side B: "))
C = float(input("Enter the length of side C: "))


if A + B > C and A + C > B and B + C > A:
    
    if A == B == C:
        print("The triangle is Equilateral.")
    
    elif A == B or B == C or A == C:
        print("The triangle is Isosceles.")
    
    else:
        print("The triangle is Scalene.")
    
    
    if (A**2 + B**2 == C**2) or (A**2 + C**2 == B**2) or (B**2 + C**2 == A**2):
        print("The triangle is Right Angled.")
else:
    print("The sides do not form a valid triangle.")

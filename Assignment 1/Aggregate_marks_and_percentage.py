subject_1 = float(input("Enter the marks of subject 1: "))

subject_2 = float(input("Enter the marks of subject 2: "))

subject_3 = float(input("Enter the marks of subject 3: "))

subject_4 = float(input("Enter the marks of subject 4: "))

subject_5 = float(input("Enter the marks of subject 5: "))

Aggregate_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

Percentage = (Aggregate_marks/500) * 100

print(f"Aggregate marks of student: {Aggregate_marks}")

print(f"Percentage of student: {Percentage}%")
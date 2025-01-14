basic_salary = float(input("Enter the basic salary of Ramesh: "))

Dearness_allowance = basic_salary * 0.40

House_rent_allowance = basic_salary * 0.20

gross_salary = basic_salary + House_rent_allowance + Dearness_allowance

print(f"Gross salary of Ramesh: {gross_salary}")
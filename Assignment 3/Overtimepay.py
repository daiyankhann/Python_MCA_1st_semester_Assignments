OVERTIME_RATE = 12.00
REGULAR_HOURS = 40


employee_hours = []

print("Enter the hours worked by each employee (whole numbers only):")
for i in range(1, 11):
    while True:
        try:
            hours = int(input(f"Employee {i}: "))
            if hours < 0:
                print("Hours cannot be negative. Please enter a valid number.")
            else:
                employee_hours.append(hours)
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")


print("\nOvertime Pay Details:")
for i, hours in enumerate(employee_hours, start=1):
    overtime_hours = max(0, hours - REGULAR_HOURS)  
    overtime_pay = overtime_hours * OVERTIME_RATE  
    print(f"Employee {i}: Worked {hours} hours, Overtime hours: {overtime_hours}, Overtime pay: Rs. {overtime_pay:.2f}")
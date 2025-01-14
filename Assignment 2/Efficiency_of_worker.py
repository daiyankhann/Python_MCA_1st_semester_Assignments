Time_taken = float(input("Enter the time taken by the worker (in hours): "))

if 2 <= Time_taken < 3:
    print("The worker is Highly Efficient.")
elif 3 <= Time_taken < 4:
    print("The worker is ordered to improve speed.")
elif 4 <= Time_taken < 5:
    print("The worker is given training to improve speed.")
elif Time_taken >= 5:
    print("The worker has to leave the company.")
else:
    print("Invalid input. Time taken cannot be less than 2 hours.")

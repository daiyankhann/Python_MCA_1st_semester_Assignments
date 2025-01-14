def calculate_sums(numbers):
    positive_sum = 0
    negative_sum = 0

    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    return positive_sum, negative_sum
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

positive_sum, negative_sum = calculate_sums(numbers)
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
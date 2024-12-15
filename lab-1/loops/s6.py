def sum_of_numbers(numbers):
    total = 0  # Initialize the sum variable
    for num in numbers:  # Loop through each number in the list
        total += num  # Add each number to the total
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_of_numbers(numbers)
print(f"The sum of the numbers in the list is: {result}")

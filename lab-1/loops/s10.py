def sum_positive_numbers():
    total_sum = 0  # Variable to store the sum
    while True:  # Infinite loop to keep asking for input
        number = float(input("Enter a positive number (or a negative number to stop): "))  # Accept user input
        
        if number < 0:  # If the entered number is negative, break the loop
            break
        
        total_sum += number  # Add the positive number to the total sum
    
    return total_sum

# Example usage
result = sum_positive_numbers()
print(f"The total sum of the entered positive numbers is: {result}")

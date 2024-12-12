def find_max_value(numbers):
    """
    Returns the maximum value from a list of integers.
    
    :param numbers: List of integers
    :return: Maximum value in the list
    """
    if not numbers:
        raise ValueError("The list is empty. Please provide a list with at least one integer.")
    return max(numbers)

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("The maximum value is:", find_max_value(numbers))

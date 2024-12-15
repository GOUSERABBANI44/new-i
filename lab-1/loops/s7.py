def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # Vowels to check for
    count = 0  # Variable to store the number of vowels

    for char in input_string:  # Iterate over each character in the string
        if char in vowels:  # If the character is a vowel
            count += 1  # Increment the count for each vowel

    return count

# Example usage
input_string = "Hello, World!"
result = count_vowels(input_string)
print(f"The number of vowels in the string is: {result}")

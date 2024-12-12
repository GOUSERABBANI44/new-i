# Input string
input_string = "Hello, welcome to the world of Python!"

# Substring to check
substring = "WELCOME"

# Converting the string to uppercase
uppercase_string = input_string.upper()

# Checking if the substring is in the uppercase string
contains_substring = substring in uppercase_string

# Displaying the results
print(f"Original string: {input_string}")
print(f"Uppercase string: {uppercase_string}")
print(f"Does the string contain '{substring}'? {contains_substring}")

correct_password = "secret123"  # The correct password
max_attempts = 3  # Maximum number of attempts
attempts = 0  # Number of attempts made by the user

while attempts < max_attempts:  # Loop until the user runs out of attempts
    guess = input("Enter the password: ")  # Accept user input
        
    if guess == correct_password:  # Check if the guess is correct
        print("Congratulations! You guessed the correct password.")
        break  # Exit the loop if the guess is correct
    else:
        attempts += 1  # Increment the number of attempts
        print(f"Incorrect password. You have {max_attempts - attempts} attempt(s) left.")
    
if attempts == max_attempts:  # If the user has used all attempts
    print("Sorry! You've used all your attempts. The correct password was:", correct_password)


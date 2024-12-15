
correct_password = "Rabbani123"
max_attempt = 3
attempts = 0
while attempts < max_attempt:
    guess = input("enter a password: ")
    if guess == correct_password:
        print("Your entered correct password")
        break
    else:
        attempts += 1
        print(f"You entered wrong password and you have {max_attempt - attempts} attempts...")

if max_attempt == attempts:
    print("Sorry your maximum attempts are over try again later....... ")


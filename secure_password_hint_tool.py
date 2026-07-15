print("\nThe Secure Password Hint Tool\n")  

#collecting user input
password = input("Enter your secret password: ").strip()

#processing
first_letter = password[0].upper()
last_letter = password[-1].upper()

print(f"Your password hint: It starts with {first_letter} and ends with {last_letter}.")

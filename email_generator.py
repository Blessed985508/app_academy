#creating a professional system email generator
first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username= f"{first[0]}{last}"  

print(f"Your email address is: {username.lower()}@university.co.za")
#Collecting the user information
print("\nStudent Profile Card\n")
name=input("what is your name: ")
surname=input("what is your surname: ")
age=int(input("what is your age: "))
favNum=float(input("what is your favourite number: "))

#full name
fullName=f"{name} {surname}"

#Greetings
print(f"\nWelcome, {fullName}!")

#String manipulation
print(f"Your name in uppercase: {fullName.upper()}")
print(f"Your name in title case: {fullName.title()} ")

#Arithmetic
age*=12
print(f"Your age in months is: {age}")

#Rounding your favourite number to 2 decimal places
roundedNum=round(favNum , 2)
print(f"Your favourite number rounded to 2 decimal places is: {roundedNum}")

#Output
print("\nData Types:")
print(f"First name: {type(name)}")
print(f"Surname: {type(surname)}")
print(f"Your age is: {type(age)}")
print(f"Your favourite number is: {type(favNum)}")
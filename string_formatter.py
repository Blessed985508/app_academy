print("String Formatter\n")

#Collecting User Input
name = input("Enter your name: ").strip()
last_name = input("Enter your last name: ").strip()
bio = input("Write a short message bio: ").strip()

#creating a username
username = f"{name[0].lower()}{last_name.lower()}"
full_name = f"{name.title()} {last_name.title()}"

#counting the number of characters in a string
bio_length = len(bio) 

#replacing words in a string
bio = bio.replace("I am","I’m")

#Output            
print(f"\n-------- User Profile --------")
print(f"Your full name is: {full_name}")
print(f"Your bio states: {bio}")
print(f"Your bio length is: {bio_length} characters")
print(f"Your username is: {username}")
             
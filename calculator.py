#collecting user input

num1 = float(input("Enter first number:"))
num2 =float(input("Enter second number: "))

# Display heading
print("\n========== CALCULATOR RESULTS ==========\n")

#Basic operations
print(f"Addition(+)\t\t :   {round((num1 + num2),2)}")
print(f"Subtration(-)\t\t : {round((num1 - num2),2)}")
print(f"multiplication(*)\t : {round((num1*num2) ,2 )}")

#division operations
if num2 != 0:
    print(f"division(/)\t\t: {round((num1/num2) ,2 )}") 
    print(f"floor_division(//)\t: {round((num1//num2) ,2 )}")
    print(f"modulus(%): {round((num1%num2) ,2 )}")
else:
    print("Division (/)\t\t: Cannot divide by zero.")
    print("Floor Division (//)\t: Cannot divide by zero.")
    print("Modulus (%)\t\t: Cannot divide by zero.")

print("\n========================================")
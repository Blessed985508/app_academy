#grade classifier

#collecting user input
name = input("Enter your name: ")

PPB_marks = float(input("Enter your marks for PPB: "))
CFB_marks = float(input("Enter your marks for CFB: "))
DCT_marks = float(input("Enter your marks for DCT: "))

#calculating the overall average
average = (PPB_marks + DCT_marks + CFB_marks)/3

#calculating the marks

grade = ""
status = ""
if average >=80: 
    grade = "A"
    status = "PASS"

    
elif average >=70: 
    
    grade = "B"
    status = "PASS"
    
elif average >=60 : 
    
    grade = "C"
    status = "PASS"

elif average >=50 : 
    grade = "D"
    status = "PASS"

else: 
    print("You did not pass , Your average is less than 50")
    grade = "F"
    status = "FAIL"

intervention = []

if PPB_marks < 40:
    intervention.append("PPB")

if DCT_marks < 40:
    intervention.append("DCT")

if CFB_marks < 40:
    intervention.append("CFB")   

#display the results 

print("\n---------THE SCHOOL REPORT--------------\n")
print(f"Learner name:\t {name}" )
print(f"PPB marks: {PPB_marks}")
print(f"DCT marks: {DCT_marks}")
print(f"CFB marks: {CFB_marks}")
print(f"The overall average : {round(average,2)}")
print(f"The grade : {grade}")
print(f"Status:  {status}")
print(f"Intervention flags : {intervention}" )


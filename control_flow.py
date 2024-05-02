######## If else ########

cgpa = float(input("Enter your cGPA: "))

if cgpa == 5:
    print("Your grade is 'A+'")
elif 4 <= cgpa < 5:
    print("Your grade is 'A'")
elif 3 <= cgpa < 4:
    print("Your grade is 'B'")
elif 2 <= cgpa < 3:
    print("Your grade is 'C'")
elif 1 <= cgpa < 2:
    print("Your grade is 'D'")
elif 0 < cgpa < 1:
    print("Your grade is 'E'")
elif cgpa == 0:
    print("Your grade is 'Fail'")
else:
    print("Invalid cgpa")  


#this is a simple grading system for students
print("WELCOME TO YOUR VIRTUAL GRADING SYSTEM FOR STUDENTS ")
name = input('Please enter your name: ')  #get's your name from you
mark = input('Please enter your mark : ') #get's your mark from you

m = float(mark) #make numbers in decimals too get a grade
if m > 100:
    print(f"{name}, That's not a right mark input")
elif m >= 80:
    print(f'{name}, Your grade is an A')
elif m >= 70:
    print(f'{name}, Your grade is a B2')
elif m >= 75:
    print(f'{name}, Your grade is a B3')
elif m >= 70:
    print(f'{name}, Your grade is a C4')
elif m >= 65:
    print(f'{name}, Your grade is a C5')
elif m >= 60:
    print(f'{name}, Your grade is a C6')
elif m >= 55:
    print(f'{name}, Your grade is a D7')
elif m >= 45:
    print(f'{name}, Your grade is an E8')     
else:
    print(f'{name}, Your grade is an F9')


# ~by Dessy


lights = "blue"

if(lights=="red"):
    print("Stop")
elif(lights=="yellow"):
    print("Look")
elif(lights=="green"):
    print("Go")
else:
    print("Lights are broken")
print("End of code")



#Grade students based on marks

marks = float(input("Enter the Marks : "))

if(marks>=90):
    print("Grade = A")
elif(90>marks>=80):
    print("Grade = B")
elif(80>marks>=70):
    print("Grade = C")
else:
    print("Grade = D")
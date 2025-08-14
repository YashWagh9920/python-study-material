class student:
    def information():
        name=input("enter the name of the student:-")
        age=int(input("enter the age of the student:-"))
        marks=float(input("enter total marks:-"))
        print("NAME OF STUDENT:-",name)
        print("AGE OF STUDENT:-",age)
        print("TOTAL MARKS OF STUDENT:-",marks)
obj=student
obj.information()

names=()
roll_number=()
maths=()
science=()
english=()
print("1.To add information of N nuber of students(Name,Roll number,3 subject marks)\n\n2.To display student's roll number and marks whose name is 'python'\n\n3.To perform nested tuples and Sort nested tuple by name.\n\n4.press(4)for exit")
while True:
    x=int(input("enter your choice:-"))
    if x==1:
        lim=int(input("enter the number of students:-"))
        print("enter the name of students:-")
        for i in range(0,lim):
            ele=input()
            names=names+(ele,)
        print("enter roll number of students:-")
        for i in range(0,lim):
            ele=int(input())
            roll_number=roll_number+(ele,)
        print("enter the marks of maths of",lim,"students")
        for i in range(0,lim):
            ele=int(input())
            maths=maths+(ele,)
        print("enter the marks of science of",lim,"students")
        for i in range(0,lim):
            ele=int(input())
            science=science+(ele,)
        print("enter the marks of science of",lim,"students")
        for i in range(0,lim):
              ele=int(input())
              english=english+(ele,)
        print("NAME OF THE STUDENTS:-",names)
        print("ROLL NUMBER OF STUDENTS:-",roll_number)
        print("MATHEMATICS MARKS OF ABOVE STUDENTS:-",maths)
        print("SCIENCE MARKS OF ABOVE STUDENTS:-",science)
        print("ENGLISH MARKS OF ABOVE STUDENTS:-",english)
    elif x==2:
        student_names=()
        student_number=()
        student_marks=()
        lim=int(input("enter the number of students:-"))
        print("enter the name of students:-")
        for i in range(0,lim):
            ele=input()
            student_names=student_names+(ele,)
        print("enter the roll number of students:-")
        for i in range(0,lim):
            ele=int(input())
            student_number=student_number+(ele,)
        print("enter total marks of students:-")
        for i in range(0,lim):
            ele=int(input())
            student_marks=student_marks+(ele,)
        for i in range(0,lim):
            if student_names[i]=="python":
                index=i
                flag=1
                break
            else:
                flag=0
        if flag==1:
             print("Student with name 'python' is present")
             print("Roll Number is:-",student_number[index])
             print("total marks are:-",student_marks[index])
        else:
             print("Student with name 'python' is not present")
    elif x==3:
        nested_tupple=()
        tuple1=()
        lim1=int(input("enter the size of tupple:-"))
        for i in range(0,lim1):
            fruit_name=input("enter fruit names:-")
            fruit_colour=input("enter colour of fruits:-")
            fruit_quant=int(input("enter quantity of fruits:-"))
            tuple1=(fruit_name,fruit_colour,fruit_quant)
            nested_tupple=nested_tupple+(tuple1,)
        print("tupple before sorting:-",nested_tupple)
        print("tupple after sorting:-",sorted(nested_tupple))
    elif x==4:
        break
    else:
        print("invalid option enter valid option")
    
        
     
          
    
    
    
     
    
                     
        
        
        
        
        
    
        
    
                
        
         
    
    



                 
                 
                 
                 
            
                 
                 
     
                
                
                
                

        
        
        
   
        
        
        
        
        
     
          
    
    
    
     
    
                     
        
        
        
        
        
    
        
    
                
        
         
    
    



                 
                 
                 
                 
            
                 
                 
     
                
                
                
                

mylist=[]
n=int(input("enter the size of list:-"))
print("enter the elementss of list:-")
for i in range(0,n):
    ele=int(input())
    mylist.append(ele)
print("the list is:-",mylist)
print("1.create list of odd elements\n2.create list of even elements\n3.merge the two lists\n4.sort the two lists\n5.Update first element of list  with X value\n6.delete the middle element of the list\n7.Find the min and max from the list\n8. Add N names into the existing number list and check if whether python name is present or not\n9.press 9 for exit")
while True:
    x=int(input("enter your choice:-"))
    if x==1:
        oddlist=[i for i in mylist if i%2!=0]
        print(oddlist)
    elif x==2:
        evenlist=[i for i in mylist if i%2==0]
        print(evenlist)
    elif x==3:
        list1=[]
        list2=[]
        list3=[]
        lim1=int(input("enter the limit of the first list:-"))
        print("enter the elements of first list:-")
        for i in range(0,lim1):
            ele=int(input())
            list1.append(ele)
        lim2=int(input("enter the limit of second list:-"))
        print("enter the elements of the second list:-")
        for i in range(0,lim2):
            ele=int(input())
            list2.append(ele)
        list3=list1+list2
        print("the merged list is:-",list3)
    elif x==4:
        list1=[]
        list2=[]
        list3=[]
        lim1=int(input("enter the limit of the first list:-"))
        print("enter the elements of first list:-")
        for i in range(0,lim1):
            ele=int(input())
            list1.append(ele)
        lim2=int(input("enter the limit of second list:-"))
        print("enter the elements of second list:-")
        for i in range(0,lim2):
            ele=int(input())
            list2.append(ele)
        list3=list1+list2
        list3.sort()
        print("the sorted list is:-",list3)
    elif x==5:
        a=int(input("enter value which is to be replaced with first element of list:-"))
        print("list before replacing:-",mylist)
        mylist[0]=a
        print("list after replacing:-",mylist)
    elif x==6:
        if len(mylist)%2==0:
            mid=len(mylist)//2
        else:
            mid=len(mylist)//2
        print("list before deleting middle element:-",mylist)
        mylist.pop(mid)
        print("list after deleting middle element:-",mylist)
    elif x==7:
        minimum=min(mylist)
        maximum=max(mylist)
        print("minimum element of list is:-",minimum,"\nmax element of list:-",maximum)
    elif x==8:
        lim=int(input("enter the number of elements to be inserted:-"))
        for i in range(0,lim):
            ele=input()
            mylist.append(ele)
        for i in range(0,len(mylist)):
            if mylist[i]=='python':
                flag=1
            else:
                flag=0
        if flag==1:
            print("python is present in the list")
        else:
            print("python is not present in the list")
    elif x==9:
        break
    else:
        print("invalid option enter valid option")
        
    
        
        
        
   
        
        
        
        
        
     
          
    
    
    
     
    
                     
        
        
        
        
        
    
        
    
                
        
         
    
    



                 
                 
                 
                 
            
                 
                 
     
                
                
                
                

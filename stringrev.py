str=input(("enter the string:-"))
print("your entered string is",str)
str1=""
for i in range(0,len(str)):
    a=str[i]
    str1=a+str1
if str==str1:
    print("given string",str,"is palindrome")
else:
     print("given string",str,"is not a palindrome")
  
    

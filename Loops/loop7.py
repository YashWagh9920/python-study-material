str = input("enter the string:-")

for i in range(0,len(str)):
    char = str[i]
    if(str.count(char) == 1):
        print(char)
        break

#----------------------------------------------------------------------

fact = int(input("enter the number whose factorial is to be found:-"))

answer = 1

for i in range(1,fact+1):
    answer *= i

print("factorial of", fact ,"is", answer)


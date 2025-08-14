str = input("enter string to be reversed:-")
reverse =""

for i in range(0,len(str)):
    reverse = str[i] + reverse

print(reverse)
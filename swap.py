a=int(input("enter first number:-"))
b=int(input("enter second number:-"))
print("numbers before swapping:-")
print("a=",a,"b=",b)
swap=a
a=b
b=swap
print("numbers after swapping:-")
print("a=",a,"b=",b)
if a<0:
    print("first number",a,"is negative")
else:
    print("first number",a,"is not negative")

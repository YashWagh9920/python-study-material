fact=int(input("enter the number whose factorial is to be found:-"))
a=fact
for i in range(1,fact):
    fact=fact*i
print("factorial of",a,"is",fact)

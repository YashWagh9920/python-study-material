number= int(input("enter number which has to be checked prime or not:-"))

count = 0

if number > 1:
    for i in range(2,number):
        if number % i == 0 :
            count += 1
else:
    print("1 is a prime number.")

if(count > 0):
    print(number ,"is not a prime number.")
elif(count == 0):
    print(number ,"is a prime number")

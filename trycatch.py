try :
   num1 = int(input("Enter the numerator :- "))
   num2 = int(input("Enter the denominator :- "))
   quo = num1/num2
   print("The quotient after division is" , quo)
except ZeroDivisionError:
   print("The denominator can never be zero ")
else :
   print("There is no error ")
finally :
   print("No error ")

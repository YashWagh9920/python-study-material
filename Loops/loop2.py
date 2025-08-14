limit = int(input("enter limit:-"))
even_number_sum = 0

for i in range(0,limit+1):
    if(i % 2 == 0):
        even_number_sum += i

print("the sum of even numbers from 0 to", limit ,"is", even_number_sum)




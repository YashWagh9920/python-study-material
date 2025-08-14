table = int(input("enter the number whose table has to be written :-"))

for i in range(1,11):
    if i == 5:
        continue
    print(table ,"x", i,"=",  i * table)


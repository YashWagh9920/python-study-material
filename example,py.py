mylist = []
n = int(input("Enter the size of the list: "))
print("Enter the elements of the list: ")
for i in range(n):
    ele = int(input())
    mylist.append(ele)
print("1.create list of odd elements\n2.create list of even elements\n3.merge the two lists\n4.sort the two lists\n5.Update first element of list  with X value\n6.delete the middle element of the list\n7.Find the min and max from the list\n8. Add N names into the existing number list and check if whether python name is present or not\n9.press 9 for exit")
while True:
    x = int(input("Enter your choice: "))
    if x == 1:
        oddlist = [i for i in mylist if i % 2 != 0]
        print(oddlist)
    elif x == 2:
        evenlist = [i for i in mylist if i % 2 == 0]
        print(evenlist)
    elif x == 3:
        list1 = []
        list2 = []
        lim1 = int(input("Enter the limit of the first list: "))
        print("Enter the elements of the first list: ")
        for i in range(lim1):
            elem = int(input())
            list1.append(elem)
        lim2 = int(input("Enter the limit of the second list: "))
        print("Enter the elements of the second list: ")
        for i in range(lim2):
            elem = int(input())
            list2.append(elem)
        list3 = list1 + list2
        print("The merged list is:", list3)
    elif x == 4:
        sorted_list = sorted(mylist)
        print("The sorted list is:", sorted_list)
    elif x == 5:
        a = int(input("Enter the value to replace the first element of the list with: "))
        print("List before replacing:", mylist)
        mylist[0] = a
        print("List after replacing:", mylist)
    elif x == 6:
        mid = len(mylist) // 2
        print("List before deleting middle element:", mylist)
        mylist.pop(mid)
        print("List after deleting middle element:", mylist)
    elif x == 7:
        min_val = min(mylist)
        max_val = max(mylist)
        print("Minimum element of the list is:", min_val)
        print("Maximum element of the list is:", max_val)
    elif x == 8:
        names = ["Python"]
        for name in names:
            if name in mylist:
                print(f"{name} is present in the list.")
            else:
                print(f"{name} is not present in the list.")
    elif x == 9:
        break
    else:
        print("Invalid option. Please choose a valid number.")

lst =["apple","banana","mango","apple","orange"]

for items in lst:
    count =lst.count(items)
    if count > 1:
        print("this item is duplicate in list", items)
        break
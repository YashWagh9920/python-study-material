import sys
class Experiment:
    def stringinput(self):
        str1 = str(input("Enter the first string "))
        str2 = str(input("Enter the second string "))
        print("Strings after getting converted into set : ")
        str1_set = set(str1)
        str2_set = set(str2)
        print("The set string 1 is :" ,str1_set)
        print("The set string 2 is : " ,str2_set)
    
    def set_union(self):
        str1 = str(input("Enter the first string "))
        str2 = str(input("Enter the second string "))
        print("Strings after getting converted into set : ")
        str1_set = set(str1)
        str2_set = set(str2)
        print("The set string 1 is :" ,str1_set)
        print("The set string 2 is : " ,str2_set)
        print("The two set union is " , str1_set | str2_set )
    
    def set_intersection(self):
         str1 = str(input("Enter the first string "))
         str2 = str(input("Enter the second string "))
         print("Strings after getting converted into set : ")
         str1_set = set(str1)
         str2_set = set(str2)
         print("The set string 1 is :" ,str1_set)
         print("The set string 2 is : " ,str2_set)
         print("The two set intersection is " , str1_set & str2_set )

    def set_differnce(self):
         str1 = str(input("Enter the first string "))
         str2 = str(input("Enter the second string "))
         print("Strings after getting converted into set : ")
         str1_set = set(str1)
         str2_set = set(str2)
         print("The set string 1 is :" ,str1_set)
         print("The set string 2 is : " ,str2_set)
         print("The difference between set1 from set2 " , str1_set - str2_set )   

    def set_symmetricdiffernce(self):
         str1 = str(input("Enter the first string "))
         str2 = str(input("Enter the second string "))
         print("Strings after getting converted into set : ")
         str1_set = set(str1)
         str2_set = set(str2)
         print("The set string 1 is :" ,str1_set)
         print("The set string 2 is : " ,str2_set)
         print("The two set's symmetric  difference is " , str1_set ^ str2_set )

obj1 = Experiment()
def call():
     while True:
          print("Press 1 : For Creating two strings ")
          print("Press 2 : For Displaying Set Union of two strings")
          print("Press 3 : For displaying Set intersection of two strings")
          print("Press 4 : For Illustrating Set difference between two strings")
          print("Press 5 : For dispalying symmetric difference of two strings")
          print("Press 6 : For exiting")
          choice = int(input("Enter the choice : "))
          if choice == 1 :
               obj1.stringinput()
          elif choice == 2:
               obj1.set_union()
          elif choice == 3 :
               obj1.set_intersection()
          elif choice == 4 :
               obj1.set_differnce()
          elif choice == 5 :
               obj1.set_symmetricdiffernce()
          elif choice == 6:
               sys.exit()

call()

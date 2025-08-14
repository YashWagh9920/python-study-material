import sys 
class Experiment: 
    def create_dictionary(self):
        dictionary = {}
        lim = int(input("Enter the number of key:value pairs"))
        for i in range(0,lim):
            key=input("Enter the key Name ")
            value=input("Enter the value of the key ")
            dictionary[key]=value
        print("The dictionary is :\n" , dictionary)

    def exercise_on_dictionary(self):
            dictionary = {}
            lim = int(input("Enter the number of key:value pairs"))
            for i in range(0,lim):
               key=input("Enter the key ")
               value=input("Enter the value of the key ")
               dictionary[key]=value
            print("The dictionary is :\n" , dictionary)
            print("Concatenating another Key:Value pair")
            key = input("Enter the key  that is to be added :")
            value =input("Enter the value of the key ")
            dictionary[key]=value
            print("The dictionary is :\n" , dictionary)
            print("Deleting a particular Key:Value pair ")
            key = input("Enter the key of the key:value pair  that is to be deleted : ")
            dictionary.pop(key)
            print("The dictionary after deleting the key:valure pair " ,dictionary)

            
    def traversing_dictionary(self):
            dictionary = {}
            lim = int(input("Enter the number of key:value pairs"))
            for i in range(0,lim):
               key=input("Enter the key ")
               value=input("Enter the value of the key ")
               dictionary[key]=value
            print("The dictionary is :\n" , dictionary)
            found_value = input("Enter the value that is to be found : ")
            for i in dictionary:
                 if dictionary[i] == found_value :
                      print("The value is found ")
                 elif(i == lim-1 and dictionary[i] != found_value ):
                      print("Element not found ")

    def maplist_dictionary(self):
         dictionary = {}
         lim = int(input("Enter the number of key-value pairs in the dictionary: "))
         for i in range(lim):
              key = input("Enter the key: ")
              value = []
              limlist = int(input("Enter the limit of list : "))
              print("Enter the values of list : ")
              for i in range(0,limlist):
                  ele=input()
                  value.append(ele)
              dictionary[key] = value
         print("The dictionary is : " , dictionary)

obj1 = Experiment()
def call():
     while True:
        print("Press 1 - For Creating a Dictionary  ")
        print("Press 2 - For Updating and Deleting aa key:value pair")
        print("Press 3 - For finding a key:value pair ")
        print("Press 4 - For mapping 'n' list in dictionary ")
        print("Press 5 - For exiting ")
        choice = int(input("Enter your choice"))
        if choice == 1:
          obj1.create_dictionary()
        elif choice == 2:
          obj1.exercise_on_dictionary()
        elif choice == 3:
          obj1.traversing_dictionary()
        elif choice == 4:
          obj1.maplist_dictionary()
        elif choice == 5:
            sys.exit()

call()

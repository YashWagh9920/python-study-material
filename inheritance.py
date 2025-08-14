class Father():
    def father_info(self):
        self.father_name = str(input("Enter the name of the father: "))
        self.father_age = int(input("Enter the age of father: "))

class Mother():
    def mother_info(self):
        self.mother_name = str(input("Enter the mother's name: "))
        self.mother_age = int(input("Enter the age of the mother: "))

class Child(Father, Mother):
    def son_info(self):
        son_name = str(input("Enter the son's name: "))
        son_age = int(input("Enter the age of the son: "))
        print("The father of", son_name, "is", self.father_name)
        print("The mother of", son_name, "is", self.mother_name) 
        print("The age of father is", self.father_age)
        print("The age of mother is", self.mother_age)

obj1 = Child() 
obj1.father_info() 
obj1.mother_info() 
obj1.son_info() 

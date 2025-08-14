class grandfather:
    def ginfo(self):
        self.gname=input("enter name of grandfather:-")
        self.gage=int(input("enter age of grandfather:-"))
class father(grandfather):
    def finfo(self):
        self.fname=input("enter name of father:-")
        self.fage=int(input("enter age of father:-"))
class son(father):
    def sinfo(self):
        self.sname=input("enter name of son:-")
        self.sage=int(input("enter age of son:-"))
        print("grandson of",self.gname,"is",self.sname)
        print("son of ",self.fname,"is",self.sname)
        print("age of grandfather is:-",self.gage)
        print("age of father is:-",self.fage)
        print("age of son is:-",self.sage)
obj=son()
obj.ginfo()
obj.finfo()
obj.sinfo()

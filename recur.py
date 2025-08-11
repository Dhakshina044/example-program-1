class stduent:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def details(self):
        print("name=",self.name,"age=",self.age,"mark=",self.mark)
std1=stduent("kumar",20,345)
std2=stduent("Anath",20,467)
std1.details()
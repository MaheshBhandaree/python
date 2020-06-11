class Computer:#class name
    def __init__(self,cpu,ram):#CONSTRUCTOR
        self.cpu= cpu
        self.ram= ram
    def Specification(self,):
        print("The config cpu:{},and ram:{}".format(self.cpu,self.ram))
com1=Computer("i5",10)#OBJECT
com2= Computer("Mac",50)



com1.Specification()#CALLING METHODS FROM obJECT
com2.Specification()


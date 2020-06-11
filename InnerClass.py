class Student:

    def __init__(self,name,rollno):
        self.name= name
        self.rollno= rollno
        self.lap= self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.name= "lenevo"
            self.ram = "128"
            self.cpu="circle"
        def show(self):
            print(self.ram,self.cpu,self.name)


s1=Student("mahesh",132)
s2=Student("Adil,",123)

s1.show()
s2.show()

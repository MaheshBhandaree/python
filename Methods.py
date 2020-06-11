from builtins import classmethod


class Student:
    schoolname="donbosco"#class variable

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):#instance method belongs to instance varible
       return (self.m1+self.m2+self.m3)/3
    @classmethod
    def Schoolinfo(cls):#class mathod belongs to class only
        return cls.schoolname
    @staticmethod#Static maethod Does not belongs to any Class variable anfd any Instance variable
    def info():
        print("This is Student Class")


s1=Student(12,34,13)
s2=Student(12,5,21)

print(s1.avg())
print(s2.avg())
print(Student.schoolname)
Student.info()
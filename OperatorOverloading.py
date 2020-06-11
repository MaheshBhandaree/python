class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __sub__(self, other):
        n1= self.m1-other.m1
        n2= self.m2-other.m2
        s4= Student(n1,n2)
        return s4
    def __gt__(self, other):
        l1=self.m1+other.m2
        l2=self.m1+other.m2
        if l1>l2:
            return True
        else:
            return False
    def __str__(self):
        return "{},{}".format(self.m1,self.m2)


s1 = Student(2,10)
s2= Student(3,4)
s3 =s1+s2
s4 = s1-s2
print(s4.m1)
print(s3.m1)
if s1> s2:
    print("s1 is greater")
else:
    print("S2 is greater")
a=9
print(a)
print(s1.__str__())

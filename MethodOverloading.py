class A:
    def __init__(self,m1,m2):
        self.m1 =m1
        self.m2 =m2
    def add(self,a=None,b=None,c=None):
        if a!= None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!= None:
            return a+b
        elif a!=None:
            return a
            return a
s1= A(102,23)
print(s1.add(12))


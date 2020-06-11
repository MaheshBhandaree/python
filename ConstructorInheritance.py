class A:
    def __init__(self):
        print("Inint method of A")
    def feature1(self):
        print("hello1")
        print("hello2")
    def feature2(self):
        print("hi1")
        print("hi2")
class B():
    def __init__(self):
        # super().__init__()
        print("Inint method of B")
    def feature3(self):
        print("GOod Morning")
        print("Good Morning")
    def feature4(self):
        print("Good day1")

class C(A,B):
    def __init__(self):
        super(C, self).__init__()#it gives the init method of A bY Method resolution ordeer(Mro)
        print("Init Method Of C")
        
a1= C()

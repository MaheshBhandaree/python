class A:
    def show(self):
        print("In A sHow method")
class B(A):
    def show(self):
        print("IN b Show method")
    pass
s1= B()
s1.show()
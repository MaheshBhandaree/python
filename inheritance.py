class A:
    def greet1(self):
        print("Hello Good morinig")
        print("Hi Whats,up")
    def greet2(self):
        print("hey there")

class B(A):
    def greet3(self):
        print("Good Afternoon")
        print("Have you done your breakfast")
    def greet4(self):
        print("How are you")

class c(B):
    def greet(self):
        print("Hello Good  night")
        print("Bye")

a1= A()
a2=A()
a2 =B()
# a2.greet1()
# a2.greet2()
a3=c()
a3.greet1()
a3.greet2()

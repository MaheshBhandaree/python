class Car:
    engin=1200
    def __init__(self):
        self.mil= 10
        self.Com="mercedse"

c1=Car()
c2=Car()
mil= 8
Car.engin=1000
print(c1.mil,c1.Com,c1.engin)
print(c2.mil,c2.Com,c2.engin)
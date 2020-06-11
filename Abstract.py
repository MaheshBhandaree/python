from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(computer):
    def process(self):
        print("Its Running")

class whiteboard(computer):
    def write(self):
        print("Write code")
class programmer:
    def work(self,com1):
        print("Solve bug")


com1= Laptop()
com1.process()
prog1= programmer()
prog1.work()
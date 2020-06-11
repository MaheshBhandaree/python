import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=1
def greet():
    global i
    i=i+1
    print("Hello :",i)
    greet()
greet()
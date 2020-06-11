def greet():
    print("hello")
    print("good morning")
greet()
def add_sub(a,b):
    c= a+b
    d= a-b
    return c,d
result1,result2=add_sub(4,5)
print("Additon is",result1,"substracion is",result2)
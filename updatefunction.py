def update(x):
    print(id(x))
    print(x)
    x=11
    print(id(x))
    print("x",x)


a=10
update(10)
print(id(a))
print("a",a)
print("##############################")

def update1(lst):
    print(id(lst))
    print("before update",lst)
    lst[1]=25

lst=[10,20,30]
update1(lst)
print(id(lst))
print("updated ",lst)

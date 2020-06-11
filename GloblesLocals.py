a=10
print(id(a))
def somthing():
    a=9
    x= globals()['a']#makinng globle & local inside one function
    print(id(x))
    print("local variable",a)
somthing()
print("outside function ",a)
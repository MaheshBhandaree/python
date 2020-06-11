def sum(*b):
    c= 0

    for i in b:
        c=(c+i)
    print(c)
sum(5,3,24,6)
print("#################")
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("mahesh",age=28,city="mumbai",mob=982349202991)

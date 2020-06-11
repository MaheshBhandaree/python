list =[7,334,2,5,3]

itr=iter(list)
print(itr.__next__())
print(next(itr))

print("###########################")

class A:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            values=self.num
            self.num +=1
            return values
        else:
            raise StopIteration
values1=A()
for i in values1:
    print(i)

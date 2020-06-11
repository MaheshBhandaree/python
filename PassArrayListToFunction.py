lst1=[]
a=0
def soumith(lst):
        for i in lst:
            if len(i)>5:
                lst1.append(i)
                a=lst1.count(i)
        return lst1,a
lst=['sachin','virat','dhoni',"mahesh"]
lst1,a=soumith(lst)
print("valid Strings is {},and no of Valid String{}".format(lst1,a))
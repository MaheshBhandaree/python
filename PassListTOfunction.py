def count(lst):
    odd=0
    even=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst=[1,2,3,4,5,6,7,8,9,0,11]
even,odd=count(lst)
print("Even no is:{},odd no is:{}".format(even,odd))

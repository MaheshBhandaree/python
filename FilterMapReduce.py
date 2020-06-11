from builtins import map
from functools import reduce

lst=[12,23,5,21,42,314,24,52,1,42,53,4,32,11,23]

even=list(filter(lambda n:n%2==0,lst))
print("Even no Are:",even)
double=list(map(lambda n:n*2,even))
print("Double values are:",double)
addall=reduce(lambda a,b:a+b,double)
print("Add all the double Values:",addall)
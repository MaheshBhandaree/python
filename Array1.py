from array import *
vals = array('i',[12,23,4,54,5])
print(vals)
print(vals.buffer_info())
vals.reverse()
print(vals)
for i in vals:
    print(i)
print()
print("####################################")
newarr=array(vals.typecode, (a*a for a in vals))
i =0
while(i<len(newarr)):
    print(newarr[i])
    i+=1
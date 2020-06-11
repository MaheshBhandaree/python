from array import *
num=int(input("Enter The NO. Of Element you want to add:"))
arr= array('i',[])
for i in range(num):
    x=int(input("Enter the Element:"))
    arr.append(x)
# for l in arr:
#     print(l)
# print(arr)
i=0
while(i<len(arr)):
    print(arr[i])
    i+=1
val=int(input("Enter The element to search index:"))
k =0
for e in arr:
    if e == val:
        print("index is",k)
        break
    k+=1
else:
    print("Element is not Present in array")






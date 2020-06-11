from numpy import*
arr= array([2,31,2,41,345,1,35])
arr2= arr.view()# changing the address and arrays(shallo copy
print(arr)
print(arr2)
print(id(arr))
print(id(arr2))
print("####################")
arr3=array([12,4,23,5,23,4,2,2,1121,])#here we will get same address of array
arr4=arr3
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
arr5=array([1,2,3,4,55,322,4,24,24,6])#deep copy if we change onne element in array 1 it does not reflect in array 2
arr6= arr5.copy()
arr5[3]=5
print(arr5)
print(arr6)
print(id(arr5))
print(id(arr6))

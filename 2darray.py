from numpy import *
arr = array([
        [1,2,3,6,7,9],
        [4,5,6,9,7,6]

])
arr2= arr.flatten()
arr3= arr2.reshape(2,2,3)
print(arr2)
print(arr3)
print('##############33333')
m= matrix('1,2,3;4,5,6;7,8,9')
y= diagonal(m)
print(m)
print("Diagonal elemnets are",y)
print(m.min())
print()
print("###################multiplication of matrix")
z=matrix('1,2,3;6,5,8;9,6,5')
z2=matrix('1,23,3;63,5,84;96,6,15')
z3= z2*z
print(z3)
n= int(input("Enter the no of Rows"))
for i in range(1,n+1):#i represent no of elements in rows
    for j in range(1,i+1):#j represents no of *
        print('*',end='')
    print()
#print("mahesh",end='/')
############################
n=int(input("Enter The No OF rows"))
for i in range (n):
    print("*"*n)
    #for j in range (n):
     #   print("*",end="")
    #print()
##############################
n=int(input("Enter the no rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()
##############################below pattern is same as first pattern
n=int(input("Enter the no rows"))
for i in range(1,n+1):
    print("*"*i)
#########################333
n=int(input("Enter the no rows"))
for i in range(1,n+1):
    for j in range(n):
        print("*",end="")
    print()
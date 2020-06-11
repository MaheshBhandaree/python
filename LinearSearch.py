pos=-1
def search(list,n):
    i=0

    for i in range(len(list)): #while i<len(list):
        if list[i] == n:
            globals()['pos']=i
            return True
        # i+=1
    return False

list=[0,34,14,12,4]
print("Enter no to found in list and its postion")
no=int(input("Enter no"))

if search(list,no):
    print("Found At {} position".format(pos+1))
else:
    print("Not Found")
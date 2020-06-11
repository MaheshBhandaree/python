pos =-1

def search(list1, no):
    l=0
    u=len(list1)-1
    while l<=u :
        mid= (l+u)//2
        if list1[mid]==no:
            globals()['pos']=mid
            return True
        else:
            if list1[mid]<no:
                l=mid+1
            else:
                u=mid-1
    return False

list1=[0,12,13,355,466,467,656,677,897,6688]
no=int(input("Ente Element to Search"))
if search(list1,no):
    print("FOund",pos+1)
else:
    print("Not Found")

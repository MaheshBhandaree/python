no=int(input("Enter no to search"))
for i in range(2,no):
    if no %i == 0 :
        print("no is not prime")
        break
else:
    print("prime")
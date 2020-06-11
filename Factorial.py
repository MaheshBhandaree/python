
def fact(no):
    sum = 1
    if(no>=1):
        for i in range(1,no+1):
            #i=i+1
            sum= sum*i
        return sum
no= int(input("Enter Some no:"))
fact=fact(no)
print(fact)
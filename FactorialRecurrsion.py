def fact(no):
    if no==0:
        return 1
    # fact=fact*(fact(no))
    return no * fact(no-1)
no=int(input("Enter some  no"))
result=fact(no)
print(result)
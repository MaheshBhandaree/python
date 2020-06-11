s=input("Enter some String:")
n= len(s)
i=0
print("Data in forward Direction")
while i<n:
    print(s[i],end='')
    i+=1
print()
print("Data in Backward Direction")
i=n-1
while i>=0:
    print(s[i],end='')
    i-=1
print()
i=-1
while i>=-n:
    print(s[i], end='')
    i -= 1
print("###########################")
city=input("Enter Your city:")
avaicity=["hyd","punr","mumbai","delhi"]
if city.strip() in avaicity:        #.Strip() is mathod for Remove Spaces in front or back of String
    print("your city is available")
else:
    print("Your city is not Available")
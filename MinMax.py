a= int(input("Enter First no"))
b= int(input("Enter Second no"))
min=a if(a<b) else b
print("MINIMUM VALUE IS :",min)

# for MAX VAlue
a= int(input("Enter First no"))
b= int(input("Enter Second no"))
c= int(input("Enter Third no"))
max= a if a>b and a>c else b if(b>c) else c
print("Max value:",max)
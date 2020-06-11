from Calc import *
a= int(input("Enter The First no:"))
b= int(input("Enter Seccond no:"))
char=(input("Choose The Operation..\nAdd= a,A\nSub=s,S\nmul=M,m\ndiv=d,D\n"))
if char =='a'and'A':
    c=add(a,b)
    print("Addition:",c)
elif char =='s'and 'S':
    c=sub(a,b)
    print("Substraction",c)
elif char =='m'and 'M':
    c=mul(a,b)
    print("Multiplication:",c)
elif char =='D'and'd':
    c=div(a,b)
    print("Division:",c)
else:
    print("NO Choice FOund:")

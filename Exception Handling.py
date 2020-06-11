num1=int(input("Enter num1:"))
num2=int(input("Enter 1Second No:"))
try:
    print("Resourse open")
    print(num1/num2)
    no=int(input("ENter the no:"))
    print(no)
except ZeroDivisionError as e:
    print("Anything Divide  By Zero is not possible@",e)
except ValueError as e:
    print("Errror values type error ")
except Exception as e:
    print(e)
print("Resource closed")
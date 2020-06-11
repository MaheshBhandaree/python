def fib(no):
    print('Fibonacci Series:')
    a=0
    b=1
    if(no<=0):
        print("No is not valid")
    else:
        if no==1:
            print(a)
        else:
            print(b)
            for i in range(2,no):
                c=a+b
                a=b
                b=c
                if c<=100:

                    print(c)
no1= int(input("Enter range"))
fib(no1)







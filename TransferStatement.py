for  i in range(10):
    if i==7:
        print("apply break")
        break
    print(i)
print("#######################")
cart=[10,29,30,600,50,43]
for item in cart:
    if item>=600:
        print("NOt valid item above 600")
        break
    print("valid items in cart",item)
print("#######################")
    ############################Continue Statement
for  i in range(10):
    if i%2==0:
        continue
    print(i)
print("#######################")
    ##################################
cart=[10,29,30,700,50,650,43]
for item in cart:
    if item>=600:
        print("THis ",item,"is not processing")
        continue
    print("valid items in cart",item)
print("#######################")
#########################################
numbers=[10,20,0,5,15,0,25]
for i in numbers:
    if i==0:
        print("Anything divide by zero not possible")
        continue
    print("100/{}={}".format(i,100/i))
print("#######################")
##################################### pass statement(if we not requierd any content in f1() then use pass)
def f1():
   pass
def f2():
    print("hello")
f1()
f2()
########################################del statement(all the Object is delted)
x="mahesh"
y= "aMAR"
print(x)
#del x
y = None
print(x)
print(y)
################3333
s1="abc"
s2="abc"
s3="abc"
del s1
print(s2)
print(s3)
####################################3
s="""my name is "maheshbhandaree"  """
print(s)
print(s[-1])
print(s[0:10])
########################
s="mahesh"
i=0
for x in s:
    print("positve index {},negative index{}={}".format(i,i-len(s),x))
    i+=1
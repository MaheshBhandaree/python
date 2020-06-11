f = open("hell","r")
print(f.readlines())
f1 = open("abc","w")
f1.write("hello")
for data in f:
    f1.write(data)
f2= open("photo_1234.jpeg","rb")
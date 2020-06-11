def div(a,b):
    print(a/b)

def smart_div(abc):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return abc(a,b)
    return inner


div1= smart_div(div)
div1(2,8)



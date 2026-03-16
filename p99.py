a=eval(input("enter the collection:"))
b=eval(input("enter the collection:"))
c=len(b)//2
if(a == b):
    print(c)
    print(id(a))
    print(id(b))
else:
    print(a[0])
    print(a[-1])
    print(id(a))    
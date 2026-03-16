a=eval(input("enter the collection"))
if(type(a)== set):
    b=input("enter the value")
    a.add(b)
    print(a)
else:
   f=tuple(a)
   c=set(f)
   print(c)

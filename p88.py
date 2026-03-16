a =eval(input("enter the list"))
print(a)
if(type(a[0])==int and type(a[-1])==int):
    b=a[0]/3
    print(b)
    c=not(a[-1])
    print(c)
else:
    print(len(a)**2)
print("a[0]",type(a[0]))
print("a[-1]",type(a[-1]))
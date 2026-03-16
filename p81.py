a=input("enter the string:")
b=len(a)
c=list(a)
if(b%2==0):
    c.append("bye")
    print(c)    
else:
    print(a[0])
    print(a[-1])
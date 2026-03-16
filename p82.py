a=input("enter the string:")
b=len(a)
c=list(a)
if(b%2==1):
    c.insert(0,"hii")
    print(c)    
else:

    l=c.pop()
    print(c)
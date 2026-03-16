a=input("enter the string:")
b=len(a)//2
c=a[b]
d=list(a)
if(a[-1]not in("a"<=a[-1]<="z")or("A"<=a[-1]<="Z")or("0"<=a[-1]<="9")):
    print(a[::-2])
else:
    d.append(c)
    print(d)    

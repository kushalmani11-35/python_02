a=input("enter the string:")
b=len(a)//2
c=ord(a[0])
d=ord(a[b])-1
if((3<=len(a)) and(a[b] in"aeiouAEIOU") and(c%2==0) ):
    print(f"{chr(d)}")
    print(a*3)
else:
    print(f"{a*5}")    
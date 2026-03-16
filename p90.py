a=input("enter the character")
if(a[0]==a[1]):
    b=a[-2::]
    print("first string",a[0])
    print(" last string is:",a[-1])
    print("last two string are:",b)
else:
    c=len(a)//2
    d=a[::-1]
    f=d[c::]
    print(f"{f}{a[c::]}")    
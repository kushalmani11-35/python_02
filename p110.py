a=eval(input("enter the list"))
b=len(a)//2
if((a[0])%2==0 and (a[b])%2==0):
    print(a[0]+a[b])
else:
    print(a[0]-a[-1])    
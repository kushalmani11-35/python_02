a=input("enter the char:")
b=len(a)//2
if a[0] not in ("A"<=a[0]<="Z") or ("a"<=a[0]<="z") or ("0"<=a[0]<="9"):
    print(a[b])
else:
    c=a[::-1]
    print(c(a[b]))

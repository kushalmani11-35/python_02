a=input("enter the string:")

if (a in"aeiouAEIOU"):
    b=ord(a)+1
    print(chr(b))
else:
    c=ord(a)-1
    print(chr(c))
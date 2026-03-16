a=input("enter the string:")
b=(ord(a[0])+ord(a[-1]))
c=len(a)//2
if(len(a)<=10 and b%5==0):
   print(f"first letter is{ord(a[0])}")
   print(f"last letter is{ord(a[-1])}")
   print(f"middle letter is{ord(a[c])}")
else:
   print(a)
   print(a)
   print(a)       
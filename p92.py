#92. Write a program to check whether a key is present in a dictionary. If yes, 
# print its value, otherwise add the key with a new value.
a={"1":"kushal","2":"shiva","3":"lucky"}
b=input("enter the key")
if(b in a):
    print({a[b]})
else:
    c=input("enter the key ")
    a[b]=c
    print(a) 

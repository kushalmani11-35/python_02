a=list(input("enter the list:"))
b=list(input("enter the list:"))
if(a is b):
    print("last item of the second string:",b[-1])
else:
    print(f"first item of the first string:{a[0]} address{id(a)}")    
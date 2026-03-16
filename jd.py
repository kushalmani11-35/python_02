#1. Wap to check whether the char is uppercase, lowercase, digit or special char.
'''ch=input("enter a character:")
if 'A'<=ch<='Z':
    print('uppercase')
elif 'a'<=ch<='z':
    print('lowercase')
elif '0'<=ch<='9':
    print('digit')
else:
    print('special char')'''

#2. Wap to check whether the given integer is single digit or two digits or three digits or more than three digits. 
'''num=int(input("enter a number:"))
if num<10:
    print("single digit")
elif 10<num<100:
    print("two digits") 
elif 100<num<1000:
    print("three digits")
else:
    print("more than three digits")'''

#3.Wap to check the given points are lying in which quadrant.
'''x=int(input("enter x coordinate:"))
y=int(input("enter y coordinate:"))
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
else:
    print("origin")'''

#4. Wap to find the greatest of 3 numbers
'''num=float(input("enter 1st number:"))
num1=float(input("enter 2nd number:"))
num2=float(input("enter 3rd number:"))
if num>=num1 and num>=num2:
    print(num,"is greatest")
elif num1>=num and num1>=num2:
    print(num1,"is greatest")
else:
    print(num2,"is greatest")'''

#5. Wap to find the smallest of 3 numbers. 
'''num=float(input("enter 1st number:"))
num1=float(input("enter 2nd number:"))
num2=float(input("enter 3rd number:"))
if num<=num1 and num<=num2:
    print(num,"is smallest")
elif num1<=num and num1<=num2:
    print(num1,"is smallest")
else:
    print(num2,"is smallest")'''

#6.Wap to check the relation between two integer numbers
'''num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
if num1==num2:
    print("they are equal")
elif num1>num2:
    print(num1,"is greater than",num2)
else:
    print(num1,"is less than",num2)'''

#7. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, if it is digit print the reminder when  it is  divided by 3 else if it is special character print it’s ASCII value. 
'''ch=input("enter a character:")
if 'A'<=ch<='Z':
    print(chr(ord(ch)+32))
elif 'a'<=ch<='z':
    print(chr(ord(ch)-32))
elif '0'<=ch<='9':
    print(int(ch)%3)
else:
    print(ord(ch))'''

#8.Wap  to print ‘Fizz’ if the given number is multiple of three print ‘buzz’ if the given number is multiple of 5 and print ‘Fizzbuzz’ if the number is multiple of both 3 and 5
'''num=int(input("enter a number:"))
if num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print("not dicisible b both 3 and 5")'''

9# Write a program to check whether a given value is positive, negative, or neutral.
# If positive, display "Positive" with the value.
# If negative, display "Negative" with the value.
# Else, display "Neutral" with the value. 
'''num=float(input("enter a number:"))
if num>0:
    print("positive",num)
elif num<0:
    print("negative", num)
elif num==0:
    print("neutral",num)
else:
    print("invaild input")'''

#10. Write a program to check whether a given character is an alphabet, ASCII number, special character, or invalid. 
'''ch=input("enetr a character:")
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    print("alphabet")
elif '0'<=ch<='127':
    print("ASCII number")
elif ch not in ['Alphabets','Digits']:
    print("special character")
else:
    print("invalid")'''

#11. Write a program to accept any number from 1 to 5 and display the number in word form.
'''num=int("enter a nuber:")
if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
else:
    print("not between 1 to 5")'''

#12. Write a program to check which grade a given percentage belongs to. Grades: First, Second, Third, or Fail. 
'''per=float(input("enter percentage:"))
if 90<=per<=100:
    print("first")
elif 75<=per<90:
    print("second")
elif 60<=per<75:
    print("third")
elif 0<=per<60:
    print("fail")
else:
    print("invalid")'''

#13. Write a program to perform arithmetic operations based on user choice. 
'''num1=float(input("enter a number:"))
num2=float(input("enter a number:"))
op=input("enter an operator(+,-,,/,%,//,*):")
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/' and num2!=0:
        print(num1/num2)
elif op=='%' and num2!=0:
        print(num1%num2)
elif op=='//' and num2!=0:
        print(num1//num2)
elif op=='':
        print(num1**num2)
else:
    print("invalid input")'''

#14. Write a program to check whether a given collection is a list, tuple,set, or string.
# If list → append a new value in the middle.
# If tuple → append a new value at the start.
# If set → append a new value.
# Else (string) → create a new key as the given character and value as its ASCII code. 
'''val=eval(input("enter a collection:"))
if type(val)==list:
    val.append(20)
    print(val)
elif type(val)==tuple:
    print(val,"tuple is immutable")
elif type(val)==set:
    val.add(24)
    print(val)
elif type(val)==str:
    print({val:ord(val)})
else:
    print("unsupported type") '''   
    
#15. Write a program to check whether a given value is int, float, string, or other.
# If int → divide the value by 5 and display the quotient.
# If float → perform a bitwise OR operation with 15.
# If string → extract the last character and place it at the beginning.
# Else → store the value in a list and display it.
'''val=eval(input("enter a value:"))
if type(val)==int:
    print(val/5)
elif type(val)==float:
    print(int(val)|15)
elif type(val)==str:
    print(val[-1]+val[:-1])
else:
    lst=[]
    lst.append(val)
    print(lst)'''
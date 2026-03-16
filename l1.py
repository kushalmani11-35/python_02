'''def area_circle(r):
    area = 3.14 * r * r
    print("Area of circle:", area)

area_circle(5)
  '''
'''def fact(n):
    if n==1:
        return 1
    return n*(fact(n-1))
print(fact(5))'''

'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(5)'''

'''def pal(a):
    if a==a[::-1]:
        print('It is a palindrome' )
    else:
        print('It is not a palindrome')
pal('MOM')'''

'''def large(a,b,c):
    if a>b and a>c:
        print('a is largest:')
    elif b>a and b>c:
        print('b is largest:')
    else:
        print('c is largest:')
large(10,20,5)'''
'''
def vowel(a):
    count=0
    for i in a:
      if i in 'AEIOUaeiou':
        count=count+1
    print(count)
vowel('Ramu')'''

'''def rev(a):
    b=a[::-1]
    print(b)
rev('python')'''


'''def dup(a,k):
    for i in a:
        if i not in k:
            k.append(i)
    print(k)
dup([10,20,30,30,10,40],[])'''


'''def sum(*args):
    total=0
    for i in args:
        total=total+i
    print(total)
sum(10,20,30)'''

'''def use(**kwargs):
    print(kwargs)
use(n='kus',a=1345)'''

'''def user(**kwargs):
    for key,value in kwargs.items():
        print(key ,':',value )
user(name='kushal',age=1)'''

'''def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
fibonacci(10)'''

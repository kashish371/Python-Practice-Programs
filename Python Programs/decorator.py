from support_for_decorator import *
#decorators are functions through which defintion of a func can be modified
#modifying div func definition from support_for_decorator by decorator
#in decorator, func whose definition to be modifies is passed
#inner fuction is the fuction used to store the fuction returned by samrt_div
def smart_div(func):
    def inner(m, n):
        if m<n:
            m, n=n,m
        return func(m, n)
    return inner
a=int(input("enter value of a : "))
b=int(input("enter value of b : "))
c=div(a, b)
div1=smart_div(div)
d=div1(a,b)
print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

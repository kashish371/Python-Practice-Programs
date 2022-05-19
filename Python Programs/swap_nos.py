print("This script is intended to swap the values of two data variable using a third temporary variable")
a=int(input("Enter first no : "))
b=int(input("Enter second no : "))
print("Values before swapping")
print("a=",a)
print("b=",b)
temp=a
a=b
b=temp
print("Values after swapping")
print("a=",str(a))
print("b=",str(b))

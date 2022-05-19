#function overriding
def area(length, breadth):
    return length*breadth
def area(r):
    return 3.14*r*r
#gives error as area func now takes one argument
print("Area of rectangle when length=5 and breadth=10 is : ", area(5,10))
print("Area of circle when radius=6.34 is : ", area(6.34))

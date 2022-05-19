
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if(a==b==c):
    print("All values are equal")
else:
    if(a==b and a>c):
        print(a, "and", b, "are equal and greater than", c)
    elif(a==c and a>b):
        print(a, "and", c, "are equal and greater than", b)
    elif(b==c and c>a):
        print(b, "and", c, "are equal and greater than", a)
    else:
        if(a>b and a>c):
            print(a,"is bigger than", b,"and",c)
        elif(b>a and b>c):
            print(b,"is bigger than", a, "and", c)
        else:
            print(c,"is bigger than", a, "and", b)
    if(a==b and a<c):
        print(a, "and", b, "are equal and smaller than", c)
    elif(a==c and a<b):
        print(a, "and", c, "are equal and smaller than", b)
    elif(b==c and c<a):
        print(b, "and", c, "are equal and smaller than", a)
    else:

        if(a<b and a<c):
            print(a,"is smaller than", b, "and", c)
        elif(b<a and b<c):
            print(b,"is smaller than", a, "and", c)
        else:
            print(c,"is smaller than", a, "and", b)

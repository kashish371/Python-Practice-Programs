#addition of tuples
print("Addition of tuples")
t1=(1,2)
print(id(t1))
t2=(3,6)
t1=t1+t2
print(t1)
print(id(t1))

#addition of list
print("Addition of list")
t1=[1,2]
print(id(t1))
t2=[3,6]
t1=t1+t2
print(t1)
print(id(t1))

#appending one string to other
print("Appending one string to other")
t1=[1,2]
print(id(t1))
t2=[3,6]
t1.append(t2)
print(t1)
print(id(t1))

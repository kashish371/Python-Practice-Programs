from functools import reduce
"""z=lambda x, y:x+y
print(z(2,4))"""

def even(n):
    return n%2==0
list1=[2, 13, 42, 4, 524, 331, 452, 321, 22]
#using simple func
list_even=list(filter(even, list1))
print(list1)
print(list_even) 

"""or"""
#using lamda func
list_even=list(filter(lambda x:x%2==0, list1))
print(list1)
print(list_even)
#print(type of what filter returned)
list2=filter(lambda x:x%2==0, list1)
print(list2)
#to multiply each element of list_even with 2, this is done by map func
list_even2=list(map(lambda x:x*2, list_even))
print(list_even2)

#summing up all elements of list_even2, this is done by reduce function
sum=reduce(lambda x, y:x+y, list_even2)
print(sum)

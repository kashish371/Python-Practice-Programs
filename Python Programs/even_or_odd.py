a=int(input("Enter a number : "))
print(type(a))
if a==0:
    print("you entered 0 which is neither even nor odd")
elif(a%2==0):
   
    print("a is even number")
else:
    print(a%2)
    print("a is oddd number")

f=1
a=int(input("Enter a number : "))
half=int(a/2)
for i in range(2, half):
    if(a%i==0):
        print("Number is not prime")
        break
    
else:
    print("Number is prime")

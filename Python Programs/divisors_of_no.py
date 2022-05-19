n=int(input("Enter a number : "))
print("All the divisors of number are : ")
for i in range(1, n+1):
    if(n%i==0):
        print(i)

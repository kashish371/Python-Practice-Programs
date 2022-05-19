n=int(input("Enter a number : "))
fact=1
for i in range(n, 0, -1):
    fact*=i
print("Factorial of entered number is :", fact)

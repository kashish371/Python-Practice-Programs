import module_factorial as fac
n=int(input("Enter value of n : "))
r=int(input("Enter value of r : "))
def permutation(n, r):
    print("Permutation is :",fac.fact(n)/fac.fact(n-r) )
permutation(n, r)
def combination(n, r):
    print("combination is :",fac.fact(n)/(fac.fact(r)*fac.fact(n-r)))
combination(n, r)

print("\n")
print("\n")

print("----------------------WELCOME TO KASHISH'S CALCULATOR---------------------------------")
print("Which type of values you want to insert : ")
print("1. integer")
print("2. float")
v1=0
v2=0
o=0
f2=0
x=int(input("Enter your choice : "))
if(x==1):
	v1=int(input("Enter first value : "))
	v2=int(input("Enter second value : "))
elif(x==2):
	v1=float(input("Enter first value : "))
	v2=float(input("Enter second value : "))
else:
	print("Invalid choice")
	f2=1
if f2==0:
	print("Enter the choice of operation you want to perform")
	print("1. +")
	print("2. *")
	print("3. -")
	print("4. /")
	print("5. %")
	o=int(input("Enter yur choice : "))
f=0
if(v2==0 and o==4):
	print("0 value is not valid as denominator")
	f=1
if(v2==0 and o==5):
	print("0 value is not valid as denominator")
	f=1
def add(a, b):
	return(a+b)
def subs(a, b):
	return(a-b)
def mult(a, b):
	return(a*b)
def divi(a, b):
	return(a/b)
def modu(a, b):
	return(a%b)
if(f==0 and f2==0):
	if(o==1):
		sum=add(v1, v2)
		print(v1, "+", v2, "=", sum)
	elif(o==2):
		mul=mult(v1, v2)
		print(v1, "*", v2, "=", mul)
	elif(o==3):
		sub=subs(v1, v2)
		print(v1, "-", v2, "=", sub)
	elif(o==4):
		div=divi(v1, v2)
		print(v1, "/", v2, "=", div)	
	elif(o==5):
		mod=modu(v1, v2)
		print(v1, "%", v2, "=", mod)

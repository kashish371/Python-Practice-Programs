n=1
num=int(input("Enter no to print table : "))
for i in range(num, (num*10)+1, num):
    print(num, "*", n, "=", i)
    n+=1
print("\n")
count=1;
for i in range(num, (num*10)+1, num):
    print("{}*{}={}".format(n, count, i))
    count=count+1

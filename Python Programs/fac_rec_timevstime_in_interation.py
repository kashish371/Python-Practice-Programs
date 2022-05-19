print("Python script to write the execution time for a variable in a file when the variable is used to find factorial using recursion and iterative method")
import timeit
def factr(x):
	y=1
	if x==1 or x==0:
		return y
	else:
		y=x*factr(x-1)
		return y
f=open('timComp', 'w')
for i in range(4):
        #taking number
        val=int(input("Enter a value : "))
        #calculating factorial and time for recursion
        start=timeit.timeit()
        fr=factr(val)
        end=timeit.timeit()
        timer=str(end-start)
        
        #calculating factorial and time for iteration
        start=timeit.timeit()
        fact=1
        for i in range(val, 0, -1):
            fact*=i
        end=timeit.timeit()
        timei=str(end-start)
        #writing into file
        f.write("\n")
        val=str(val)
        f.write(val)
        f.write("\n")
        f.write('('+timer+","+timei+')')
       

f.close()

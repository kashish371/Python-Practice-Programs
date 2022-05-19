f=open('my_first_file.txt', 'w')
f.write('I am Kashish')
f.write("\n")
x='My name is Kashish'
f.write(x)
f.close()

f=open('my_first_file.txt', 'r')
z=f.read()
print(z)
f.close()
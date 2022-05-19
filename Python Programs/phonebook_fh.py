class contact:
    def __init__(self, fname, lname, number, email):
        self.fname=fname
        self.lname=lname
        self.number=number
        self.email=email

    def putdata(self):
        f=open('c_book.txt', 'a')
        f.write('\n'+ self.fname+' | ' +'          '+self.lname+' | '+'         '+self.number+' | '+'            '+self.email)
        f.close()
    def getdata(self):
        f=open('c_book.txt', 'r')
        data=f.read()
        print(data)
        f.close()
f=open('c_book.txt', 'w')
f.write('First Name | '+'          '+'Last Name | '+'         '+'Number | '+'            '+'Email | ')
f.close()
for i in range(2):
    fn=input('Enter first name : ')
    ln=input('Enter last name : ')
    n=input('Enter phone number : ')
    e=input('Enter email : ')
   
    contact1=contact(fn, ln, n, e)
    contact1.putdata()
contact1.getdata()

#f, l, email, cn1, cn2, address, category, delete, search, create, update, read

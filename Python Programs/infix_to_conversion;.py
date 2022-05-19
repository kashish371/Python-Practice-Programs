print("This code will convert infix expression to postfix expression and will evaluate the postfix expression to find the result")
x=input("Enter an expression: ")
operand=""
expression=[]
l=len(x)
for i in range(len(x)):
    if(x[i]>="0" and x[i]<="9"):
        operand+=x[i]
        l-=1
    elif(x[i]=='(' or x[i]==')'):
        if(operand==""):
            expression.append(x[i])
            l-=1
        else:
            expression.append(operand)
            operand=""
            expression.append(x[i])
            l-=1
    
    else:
        if(operand==""):
            expression.append(x[i])
            l-=1
        else:
            expression.append(operand)
            expression.append(x[i])
            operand=""
            l-=1
for i in range(len(x)-l, len(x)):
    if(x[i]>="0" and x[i]<="9"):
        operand+=x[i]
if(operand!=""):
    expression.append(operand)
#print(expression)
prec={'-':1,'+':2, '/':3, '*':4, '^':5}
st=[]
top=-1
tst=""
tl=[]

for v in expression:
    for val in v:
        if(val>='0' and val<='9'):
            tst+=val
    if(tst!=""):
        tl.append(tst)
        tst=""
    if(v=='('):
        st.append(v)
        top+=1
    elif(v=='+' or v=='*' or v=='/' or v=='-' or v=='%' or v=='^'):
        if(top==-1):
            st.append(v)
            top+=1
        elif(st[top]=='('):
            st.append(v)
            top+=1
        elif(prec[v]<=prec[st[top]]):
            tst+=st.pop()
            top-=1
            st.append(v)
            top+=1
            tl.append(tst)
            tst=""
        else:
            st.append(v)
            top+=1
    elif(v==')'):
        while(st[top]!='('):
            tst+=st[top]
            st.pop()
            top-=1
        tl.append(tst)
        tst=""
        if(st[top]=='('):
            st.pop()
            top-=1
while(top!=-1):
        tst+=st[top]
        st.pop()
        top-=1
tl.append(tst)
tst=""

print("Postfix expression is : ",tl)
rst=[]
top=-1
for v in tl:
    for val in v:
        if(val>='0' and val<='9'):
            tst+=val
    if(tst!=""):
        rst.append(tst)
        tst=""
    elif(v=='+' or v=='*' or v=='/' or v=='-' or v=='^'):
        if(v=='+'):
            v1=rst.pop()
            top-=1
            v2=rst.pop()
            top-=1
            rst.append(v1+v2)
            top+=1
        elif(v=='-'):
            v1=rst.pop()
            top-=1
            v2=rst.pop()
            top-=1
            rst.append(v1-v2)
            top+=1
        elif(v=='/'):
            v1=rst.pop()
            top-=1
            v2=rst.pop()
            top-=1
            rst.append(v1/v2)
            top+=1
        elif(v=='*'):
            v1=rst.pop()
            top-=1
            v2=rst.pop()
            top-=1
            rst.append(v1*v2)
            top+=1
        elif(v=='^'):
            v1=rst.pop()
            top-=1
            v2=rst.pop()
            top-=1
            rst.append(v1^v2)
            top+=1
r=rst[top]
print(r)

            

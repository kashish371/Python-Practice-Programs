#string reversal using concatination
"""s=input("Enter a string : ")
str1=""
for i in range(len(s)-1, -1, -1):
    str1=str1+s[i]
print("Reversed string : ",str1)
"""

s=input("Enter a string : ")[::-1]
print("Reversed string : ",s)



print("Welcome to my code for playing stone, paper, scissor")
import random
print("1. Rock")
print("2. Paper")
print("3. Scissor")
p1s=0
p2s=0
x="y"
while(x!="n"):
    p1=int(input("Player one \n Enter your choice : "))
    print("Player 1 : ", p1)
    p2=random.randrange(1,4)
    print("Player 2 :", p2)
    if(p1>3 or p1<1):
        print("Invalid choice")
    elif(p2>3 or p2<1):
        print("Invalid choice")
    elif(p1==1 and p2==1):
        print("Koi nhi jeeta")
    elif(p1==2 and p2==2):
        print("Koi nhi jeeta")
    elif(p1==3 and p2==3):
        print("Koi nhi jeeta")
    elif(p1==1 and p2==2):
        print("Player 2 won")
        p2s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    elif(p1==1 and p2==3):
        print("Player 1 won")
        p1s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    elif(p1==2 and p2==3):
        print("Player 2 won")
        p2s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    elif(p1==2 and p2==1):
        print("Player 1 won")
        p1s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    elif(p1==3 and p2==1):
        print("Player 2 won")
        p2s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    elif(p1==3 and p2==2):
        print("Player 1 won")
        p1s+=1
        print("Player 1 score : ", p1s)
        print("Player 2 score : ", p2s)
    print("Do you want to play again?")
    x=input("Enter y for yes and n for no : ")
    x=x.lower()
    if(x=="n"):
        print("Goodbye!!")

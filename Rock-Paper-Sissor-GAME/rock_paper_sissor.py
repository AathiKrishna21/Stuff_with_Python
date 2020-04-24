import getpass
import random

flag=0
draw=['RR','SS','PP']
one=['RS','PR','SP']
crct=['R','P','S','p','s','r']
p1=[]
p2=[]

def g1():
    flag=0
    while(1):
        print("player 1 its ur turn :")
        pl1=getpass.getpass("-->")
        if pl1 in crct:
            p1.append(pl1.upper())
            break
        else:
            print("Player 1 its an invalid charcter")
    while(1):
        print("player 2 its ur turn :")
        pl2=getpass.getpass("-->")
        if pl2 in crct:
            p2.append(pl2.upper())
            break
        else:
            print("Player 2 its an invalid charcter")       

def g2():
    flag=1
    while(1):
        print("player 1 its ur turn :")
        pl1=getpass.getpass("-->")
        if pl1 in crct:
            p1.append(pl1.upper())
            break
        else:
            print("Player 1 its an invalid charcter")
    print("Its AI's turn :")   
    print("-->*")     
    pl2=random.choice(crct)
    p2.append(pl2.upper())        

def game():
    print("Choose 1 to play with oponent:")
    print("Choose 2 to play with computer:")
    n=int(input("Enter Your Option:"))
    while(1):
        if n==1:
            for i in range(5):
                g1() 
            score()
            display(n)    
            break
        elif n==2:
            for i in range(5):
                g2()
            score()
            display(n)    
            break
        else:
            print("Enter the correct option.")

def score():
    for i in range(5):
        com="".join(p1[i])
        com=com+"".join(p2[i])
        if com in one:
            p1[i]=1
            p2[i]=0
        elif com in draw:
            p1[i]=0.5
            p2[i]=0.5
        elif com not in draw and com not in one:
            p2[i]=1
            p1[i]=0
           
def display(n):
    sc1=0
    sc2=0
    for i in range(5):
        sc1=sc1+int(p1[i])
    for i in range(5):
        sc2=sc2+int(p2[i])
    v=5-sc1-sc2   
    v=(v*0.5)
    print("***************************".center(50,' '))
    print("*       Score BOARD       *".center(50,' '))
    print("*       ***********       *".center(50,' '))
    print("*                         *".center(50,' '))
    print(f"* PLAYER-1     : {sc1+v}      *".center(50,' '))
    print("*                         *".center(50,' '))
    print(f"* PLAYER-2     : {sc2+v}      *".center(50,' '))
    print("*                         *".center(50,' '))
    print("***************************".center(50,' '))
    if n==1 and sc1>sc2:
        print("HURRAY PLAYER 1 WINS")
    elif n==1 and sc1<sc2:
        print("HURRAY PLAYER 2 WINS")
    elif n==2 and sc1<sc2:
        print("HURRAY AI WINS") 
    elif n==2 and sc1>sc2:
        print("HURRAY PLAYER WINS") 
    elif sc1==sc2:
        print(".....MATCH DRAW......")


if __name__ == "__main__": 
    print("WELCOME TO THE GAME".center(75,'*'))
    flag=0
    while(1):
        ques=input("Are you ready to play (YES/NO) : ")
        if ques.lower()=="yes":
            print("BEST OF FIVE IS WINNER".center(75,'-'))
            print("S --- STONE")
            print("P --- PAPER")
            print("R --- ROCK")
            game()
            break
        elif ques.lower()=="no":
            print("GOOD PLAY! HAVE A NICE DAY:)".center(75,''))
            break
        else:
            print("Your option is Wrong!.Select correct OPTION...")


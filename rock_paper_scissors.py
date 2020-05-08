import time
import random
print(" Welcome to the Game")

print("1. Rock")
print("2. Paper")
print("3. Scissor")
a= int(input("Enter a Number"))
if a==1:
    print(" You have Choosen Rock")
elif a==2:
    print(" You have Choosen Paper")
elif a==3:
    print(" You have Choosen Scissor")
elif a<1 or a>3:
    print(" Wrong Choice, Please select a number between 1 and 3")   
    a= int(input("Enter a Number"))
    
    
    if a==1:
        print(" You have Choosen Rock")
    elif a==2:
        print(" You have Choosen Paper")
    elif a==3: 
        print(" You have Choosen Scissor")
    
print("Taking P.C's Opinion...")
time.sleep(3)
b= random.randint(1,3)
if b==1:
    print(" PC has Choosen Rock")
elif b==2:
    print(" PC has Choosen Paper")
elif b==3:
    print(" PC has Choosen Scissor")

if a==1 and b==1:
    print("Its a Tie , Sorry No Winner")
    print(" Please Try again")
if a==2 and b==2:
    print("Its a Tie , Sorry No Winner")
    print(" Please Try again")
if a==3 and b==3:
    print("Its a Tie , Sorry No Winner")
    print(" Please Try again")

if a==1 and b==2:
    print(" PC won the Game")
if a==1 and b==3:
    print(" Congo.. You have won the Game")
if a==2 and b==1:
    print(" Congo.. You have won the Game")
if a==2 and b==3:
    print(" PC won the Game")
if a==3 and b==1:
    print(" PC won the Game")
if a==3 and b==2:
    print(" Congo.. You have won the Game")

print(" Thank You")


    

    
    


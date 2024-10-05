'''
1 for snake
-1 for water
0 for gun

'''
import random
computer = random.choice([1,-1,0])
you_choose = input("Enter your choice : ")
dict = {"s":1,"w":-1,"g":0}
reversedict = {1:"snake",-1:"water",0:"gun"}
you = dict[you_choose]
print(f"you choose {reversedict[you]} \ncomputer choose {reversedict[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==1 and you==-1):
        print("you lose!")
    elif(computer==-1 and you==1):
        print("you win!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you lose!")
    elif(computer==-1 and you==0):
        print("you win!")
    elif(computer==0 and you==-1):
        print("you lose!")
    
    else:
        print("Somenthing went wrong")
         
    



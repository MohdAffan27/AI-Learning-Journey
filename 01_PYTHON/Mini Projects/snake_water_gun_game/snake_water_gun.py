import random
"""
1 for snake
-1 for water
0 for gun
"""

computer = random.choice([1,-1,0])
user_str = input("Enter your Character (s / w / g): ")
user_dict = {"s" : 1, "w" : -1, "g" : 0}
comp_dict = {1:"snake", -1 :"water", 0:"gun"}

user = user_dict[user_str]
# by now we have 2 variables,user and computer
print("you choose",comp_dict[user],"\n computer choose ",comp_dict[computer] )

if(computer==user):
    print("Its a draw")
else:
    if(computer == 1 and user ==-1):
        print("you loose!")
    elif(computer == 1 and user == 0):
        print("you win.")
    elif(computer == -1 and user == 0):
        print("you loose!")
    elif(computer == -1 and user == 1):
        print("you Win!")
    elif(computer == 0 and user == 1):
        print("you loose!")
    elif(computer == 0 and user == -1):
        print("you win!")
    else:
        print("something went wrong!")
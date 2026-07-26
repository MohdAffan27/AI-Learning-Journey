# check and update the list
list = ["faizaan", "affan", "sahil"]

name = input("Enter your name : ")
if (name in list):
    print("Your name is already in the list.\n",list)
else:
    list.append(name)
    print("Your name was added in the list.\n", list)

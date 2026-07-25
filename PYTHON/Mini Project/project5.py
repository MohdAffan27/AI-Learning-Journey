# contact book
contacts = {}

print("-----ADD CONTACTS-----")
name = input("\nEnter contact name: ")
number= input("Enter number : ")
contacts.update({name:number})
name = input("\nEnter contact name: ")
number= input("Enter number : ")
contacts.update({name:number})
name = input("\nEnter contact name: ")
number= input("Enter number : ")
contacts.update({name:number})
name = input("\nEnter contact name: ")
number= input("Enter number : ")
contacts.update({name:number})

print("\n----ALL CONTACTS----")
print(contacts)

print("\n----SEARCH BY NAME----")
# search student
search = input("Enter the name you want to search : ")
sresult = contacts.get(search,"Incorrect name entered")
print(search,"got",sresult,"marks")

print("\n----DELETE A CONTACT----")
delete = input("enter a name you want to delete : ")
deleted = contacts.pop(delete, "CONTACT NOT FOUND")
print(delete,"got",deleted,"deleted")
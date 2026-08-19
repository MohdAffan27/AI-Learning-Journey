# book a train ticket
from  random import randint

class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def bookticket(self,fro,to):
        print(f"Train ticket is booked in train no. : {self.trainNo} from {fro} to {to} ")

    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on time.")

    def getfare(self,fro, to):
        print(f"Train ticket is booked in train no.  : {self.trainNo} from {fro} to {to} is {randint(40,45)} ")

t = train(1399)
t.bookticket("kachiguda","Nizamabad")
t.getstatus()
t.getfare("kachiguda","Nizamabad")


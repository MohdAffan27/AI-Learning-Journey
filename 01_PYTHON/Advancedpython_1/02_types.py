# Advanced type Hints
from typing import List, Tuple, Dict 


numbers: List[int] ={1,2,3,4,5} #here you can only assign integer values in the list 
print (numbers)


person: Tuple[str,int] = ("affan",504) #here you can only assign string & integer values in the tuple 
print (person)

students: Tuple[str,int] = {"affan":504} #here you can only assign string & integer values in the dictionary 
print (students)

# -----------------------------------------------------------------------------------------------------------

n : int =1# Means assign a data type to a variable

# mostly used in functions to take a Fixed variable type 
def sum(a : int,b : int): #here you can't assaign another variable type of data to to a fixed variable type
    return a+b

sum = sum(1,2)
print(sum)
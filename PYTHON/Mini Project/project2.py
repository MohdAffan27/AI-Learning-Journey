import re
#1. GEt the password input from the user 
password = input("Enter your password to check its strength : ")

#2.check each security requirement (each outputs true or false)
# checks if teh total characters lenght is 8 or more
length_check = len(password) >= 8
# Uses regular expressioms to see if at least one number exists
number_check =bool(re.search(r"\d",password))
# Uses regular expressioms to see if at least one uppercase exists
upper_case = bool(re.search(r"[A-Z]",password))
# Uses regular expressioms to see if at least onelowercase exists
lower_case = bool(re.search(r"[a-z]",password))
#3. sum up the boolean results (true act as 1, false act as 0)
total_score = length_check+number_check+upper_case+lower_case
#4. Map teh numeric score to a description without using if/else statements
strength_levels = {
    0:"very weak",
    1:"weak",
    2:"moderate",
    3:"strong",
    4:"very strong"
}
# output the result
print("your password score is :",total_score,"/4")
print("strength rating:",strength_levels)
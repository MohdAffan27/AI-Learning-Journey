# progam to find out whether a student has 
# passed or fail if it requires a total of 40% and 
# at least 33% in each subject to pass.
# assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks 1 :"))
marks2 = int(input("Enter marks 2 :"))
marks3 = int(input("Enter marks 3 :"))

# calculate marks 
percentage = (100*(marks1+marks2+marks3))/300

if(percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print("Congrats you're passed!")
else:
    print("you're failed...try again next year")
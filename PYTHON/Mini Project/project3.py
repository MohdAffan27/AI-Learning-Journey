# Students Marks Manager using lists 
std_name=[]
std_marks=[]
# ENter names
s1=input("Enter student_1 name here : ")
std_name.append(s1)
s2=input("Enter student_2 name here : ")
std_name.append(s2)
s3=input("Enter student_3 name here : ")
std_name.append(s3)
s4=input("Enter student_4 name here : ")
std_name.append(s4)
s5=input("Enter student_5 name here : ")
std_name.append(s5)
s6=input("Enter student_5 name here : ")
std_name.append(s6)
# Enter Marks  
sm1=int(input("Enter student marks here : "))
std_marks.append(sm1)
sm2=int(input("Enter student marks here : "))
std_marks.append(sm2)
sm3=int(input("Enter student marks here : "))
std_marks.append(sm3)
sm4=int(input("Enter student marks here : "))
std_marks.append(sm4)
sm5=int(input("Enter student marks here : "))
std_marks.append(sm5)
sm6=int(input("Enter student marks here : "))
std_marks.append(sm6)
# display
print(std_name)
print(std_marks)
# average
average=(sum(std_marks)+len(std_marks))/6
print("\n marks average",average)
# highest score
highest = max(std_marks)
print("highest marks : ",highest)
# lowest score
Lowest = min(std_marks)
print("lowest marks : ",Lowest)

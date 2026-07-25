# Students Marks Manager using dictionaries
d = {}
# get student details 
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})
student = input("Enter student name : ")
marks = int(input("Emte students marks : "))
d.update({student : marks})

#calculate marks
total_marks=sum(d.values())
no_of_stds = len (d)
average = total_marks/no_of_stds
print("Total marks : ", total_marks)
print("\nAverage of marks : " ,average)

#display topper and lower
highest = max(d,key=d.get)
lowest = min(d,key=d.get)

print("Highest marks are",d[highest],"scored by ",highest)
print("Lowest marks are",d[lowest],"scored by ",lowest)

# search student
search = input("enter name you want to search : ")
sresult= d.get(search,"Incorrect name")
print(search,"got",sresult,"marks")
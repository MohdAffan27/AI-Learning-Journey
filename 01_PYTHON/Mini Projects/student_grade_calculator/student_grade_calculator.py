# Total marks and percentage of a student
maths = float(input("enter marks in maths : "))
science = float(input("enter marks in science : "))
english = float(input("enter marks in english : "))
social = float(input("enter marks in social : "))
telugu = float(input("enter marks in telugu: "))
urdu = float(input("enter marks in urdu: "))

total_marks = maths+science+english+social+telugu+urdu

percentage = (total_marks/600)*100
print("total marks gained by a student are : ",total_marks)
print("with the percentage of ", percentage)